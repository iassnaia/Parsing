# from pymongo import MongoClient
# from pprint import pprint
# from pymongo.errors import *

# client = MongoClient('localhost', port = 27017)
# db = client['users']
# # db2 = client['books']
# persons = db.persons
# duplicates = db.duplicates

# doc = {"_id": "dlfjldbfb4kf",
#        "author": "Peter",
#        "age": 38,
#        "text": "its cool",
#        "tags": ['cool', 'hot', 'ice'],
#        "date": '14.06.1983'}

# try:
#     persons.insert_one(doc)
# except DuplicateKeyError as e:
#     print(e)

# authot_list = [{"author": "Pop",
#        "age": 36,
#        "text": "its  the coolss",
#        "tags": ['coolss', 'hot', 'ice'],
#        "date": '12.03.1986'},

#        {"_id": "ffhdshd5",
#        "author": "Svan",
#        "age": 24,
#        "text": "Oh  the coolss",
#        "tags": ['coolss', 'oh', 'ice'],
#        "date": '11.06.1996'},

#        {
#        "author": "SELEn",
#        "age": 27,
#        "text": "Oh  the very",
#        "date": '11.06.2000'},
# ]

#for authot in authot_list:
#    try:
#        persons.insert_one(authot)
#    except DuplicateKeyError as e:
#        duplicates.insert_one(authot)

# persons.insert_many(authot_list)

# for doc in persons.find():
#     pprint(doc)

# и
# for doc in persons.find({'author': 'Svan'}):
#     print(doc)

# или
# for doc in persons.find({"or": [{'author': 'Svan'}, {'age': 24}]}):
#     print(doc)

# сорт по автору нач. с S
# for doc in persons.find({'author': {'$regex': 'S.'}}):
#     print(doc)

# new_data = {
#     "author": "Serg",
#     "age": 56
# }

# обновить с добавлением
# persons.update_one({'author': 'Pop'}, {'$set': {'author': new_data}}) 

# persons.replace_one({'author': 'Popsa'}, new_data)

# persons.delete_many({'author': 'Andrey'})

# for doc in persons.find():
#     print(doc)

# скачать файл по ссылке
# import requests
# response = requests.get("https://gbcdn.mrgcdn.ru/uploads/asset/5560965/attachment/357f7ccb20abaeedb8ccfda8e1045098.json")

# with open('data.json', 'wb') as f:
#     f.write(response.content)

import json
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *

client = MongoClient('localhost', port = 27017)
db = client['crashes']
info = db.info

# delet base
info.delete_many({})

with open('data.json', 'r') as f:
    data = json.load(f)

count_duplicated = 0

for feature in data['features']:
    _id = feature.get('properties').get('tamainid')
    feature["_id"] = _id
    try:
        info.insert_one(feature)
    except:
        count_duplicated +=1
        print(feature)

print(count_duplicated)

count = info.count_documents({})

for doc in info.find({'properties.tamainid': 48540}):
    print(doc)

# for doc in info.find({'properties.lat2': {'$gt': 35.0, '$lt': 36.0},
#                     'properties.lon2': {'$gt': -78.0, '$lt': -77.0}}):
#     print(doc)
