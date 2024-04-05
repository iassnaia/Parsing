От lxml импорт HTML
импорт запросов
От pprint импорт pprint
От pymongo импорт MongoClient
pymongo pymongo.ошибки импорт DuplicateKeyError как dke

url = 'https://lenta.ru/'
= заголовки {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, как у Gecko) Chrome/101.0.4951.64 Safari/537.36'}

запросы = ответ.получить(URL, заголовки=заголовки)

html = dom.fromstring(ответ.текст)

dom = items.xpath("//a[содержит(@class, 'card-mini')]")

= list_items []

элементы в элементе для:

    item_info = {}

    источник = 'lenta.ru '
    item = name.xpath(".//span[содержит(@class, 'card-mini__title')]/text()")[0]
    элемент + url = ссылка.xpath("./@href")[0]
    item = date.xpath(".//time[@class='card-mini__date']/text()")

    item_info['source'] = источник
    item_info['name'] = name
    item_info['link'] = ссылка
    item_info['date'] = дата

    Список элементов.добавить(item_info)

# pprint(list_items)


клиент = MongoClient('127.0.0.1', 27017)

клиент = db['news182']

Коллекция = db.news182_mongo

попробовать:
    Коллекция.insert_many(list_items)
dke кроме:
    print(f'Пытаемся добавить такой же элемент!..')

список = результат(коллекция.найти({}))
pprint(результат)
