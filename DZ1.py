## Ознакомиться с некоторые интересными API
##Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
##Сценарий Foursquare
##Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
##Используйте API Foursquare для поиска заведений в указанной категории.
##Получите название заведения, его адрес и рейтинг для каждого из них.
##Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

#1
import requests
import json

params = {'q': 'name', 'id': '69846294'}

url = 'https://api.github.com'

user = 'iassnaia'

responce = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(responce.json(), f)

for i in responce.json():
    print(i['full_name'])


# 2. 
import requests

import json

url = 'https://api.vk.com'

method = 'friends.getOnline'

user_id = '474319172'

access_token = ''

responce = requests.get(f'{url}/method/{method}?v=5.52&access_token={access_token}')

with open('data.json', 'w') as f:
    json.dump(responce.json(), f)

print(responce.json())

{'response': [47207942]}

Для себя Парсинг сайта Auto.ru

import requests

import json

URL = 'https://auto.ru/-/ajax/desktop/listing/'

PARAMS = {
            # 'catalog_filter' : [{"mark": "BAW"}],
            'section': "used",
            'region': "moskva",
            'category': "trucks",
            'sort': "fresh_relevance_1-desc",
            'page': "pag"
        }

HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Length': '137',
    'content-type': 'application/json',
    'Cookie': '_csrf_token=1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24; autoru_sid=a%3Ag5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270%7C1580931467355.604800.8HnYnADZ6dSuzP1gctE0Fw.cd59AHgDSjoJxSYHCHfDUoj-f2orbR5pKj6U0ddu1G4; autoruuid=g5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270; suid=48a075680eac323f3f9ad5304157467a.bc50c5bde34519f174ccdba0bd791787; from_lifetime=1580933172327; from=yandex; X-Vertis-DC=myt; crookie=bp+bI7U7P7sm6q0mpUwAgWZrbzx3jePMKp8OPHqMwu9FdPseXCTs3bUqyAjp1fRRTDJ9Z5RZEdQLKToDLIpc7dWxb90=; cmtchd=MTU4MDkzMTQ3MjU0NQ==; yandexuid=1758388111580931457; bltsr=1; navigation_promo_seen-recalls=true',
    'Host': 'auto.ru',
    'origin': 'https://auto.ru',
    'Referer': 'https://auto.ru/moskva/truck/used/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'x-client-app-version': '202002.03.092255',
    'x-client-date': '1580933207763',
    'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
    'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
    'x-requested-with': 'fetch'
}


responce = requests.post(URL, json=PARAMS, headers=HEADERS)


with open('data.json', 'w') as f:
    json.dump(responce.json(), f)

print(responce.json())
