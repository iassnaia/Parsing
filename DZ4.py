from lxml import html
import requests
from datetime import datetime, timedelta
from datetime import date
from pprint import pprint
from pymongo import MongoClient
from pymongo import errors


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

client = MongoClient('localhost',27017)
db = client['news_db']  # указать имя базы данных, которая будет создана
NewsMongo = db.News # создать объект, в которую складывается коллекция News

def save_new_to_db(new):
    # Функция записи в БД. Возвращает 1, если новость быда добавлена,
    # и возвращает 0, если новость не добавлена (уже есть в БД)
    try:
        db.NewsMongo.insert_one(new)
    except errors.DuplicateKeyError:
        pass
        return 0
    else:
        return 1

def request_to_yandex():
    # Фунцкия собирает новости yandex.ru
    base_url = 'https://yandex.ru/news'
    response = requests.get(base_url, headers=header)

    dom = html.fromstring(response.text)

    # Новости собираются из 12-ти разделов
    items = dom.xpath(
        """//div[@class='mg-grid__row mg-grid__row_gap_8 news-top-rubric-stories news-app__top'] \
        //div[@class='mg-grid__col mg-grid__col_xs_4'] \
        | //div[@class='mg-grid__row mg-grid__row_gap_8 news-top-rubric-stories news-app__top'] \
        //div[@class='mg-grid__col mg-grid__col_xs_6'] \
        """)

    for item in items:
        new = {}

        # название источника
        source = item.xpath(".//a/text()")
        new['source'] = source[0].replace(u'\n', u'')

        # наименование новости
        name = item.xpath(".//h2[@class='news-card__title']/text()")
        new['name'] = name[0].replace(u'\xa0', u' ')

        #ссылка на новость
        url = item.xpath(".//a/@href")
        new['url'] = url[0]

        # дата публикации
        time_item = item.xpath(".//span[@class='mg-card-source__time']/text()")
        time = time_item[0].split(' ')[-1]
        time_v = time_item[0].split(' ')[0]
        Previous_Date = date.today() - timedelta(1)

        if time_v == 'вчера':
            new['time'] = f'{Previous_Date} {time}'
        else:
            new['time'] = f'{date.today()} {time}'

        save_new_to_db(new)


def request_to_lenta():
    # Фунцкия собирает новости lenta.ru
    base_url = 'https://lenta.ru'
    response = requests.get(base_url, headers=header)

    dom = html.fromstring(response.text)

    items = dom.xpath(
        """
        //div[@class='span8 js-main__content']//div[@class='span4'] \
        /div[@class='first-item'] \
        | //div[@class='span8 js-main__content']//div[@class='span4'] \
        /div[@class='item']
        """)

    for item in items:
        new = {}
        name = item.xpath(".//a/text()")
        url = item.xpath(".//a/@href")
        new['source'] = 'lenta.ru '
        time = item.xpath(".//time/text()")
        new['time'] = f'{date.today()} {time[0]}'
        new['name'] = name[0].replace(u'\xa0', u' ')
        new['url'] = base_url + url[0]
        save_new_to_db(new)


def request_to_mail():
    # Фунцкия собирает новости mail.ru
    base_url = 'https://news.mail.ru/'
    response = requests.get(base_url, headers=header)

    dom = html.fromstring(response.text)

    items = dom.xpath(
        """
        //div[@class='cols__inner']//span[@class='cell'] \
        | //div[@class='cols__inner']//span[@class='list__text']
        """)

    for item in items:
        new = {}
        name = item.xpath(".//span/text()")
        url = item.xpath(".//a/@href")[0]

        date_format = '%Y-%m-%dT%H:%M:%S%z'

        # Переход по новости для сбора информации
        new_more = requests.get(url, headers=header)
        dom_more = html.fromstring(new_more.text)
        source = dom_more.xpath("//a[@class='link color_gray breadcrumbs__link'] \
        //span[@class='link__text']/text()")
        if source:
            new['source'] = source[0]
        else:
            new['source'] = None

        date = dom_more.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
        if len(date) > 0:
            date = datetime.strptime(date[0], date_format)
            date = date.strftime('%Y-%m-%d %H:%M')
            new['time'] = f'{date}'
        else:
            new['time'] = None

        new['name'] = name[0].replace(u'\xa0', u' ')
        new['url'] = url
        save_new_to_db(new)

request_to_yandex()
request_to_lenta()
request_to_mail()
