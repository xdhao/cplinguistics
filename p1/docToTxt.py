import requests, pymongo
from pymongo import MongoClient, ASCENDING, DESCENDING

f = open('/home/vagrant/kr/Word2Vec/Samples/input.txt', 'w')
client = MongoClient()
database = client.v102news
news = database.news
for x in news.find( {} ).sort([('_id', ASCENDING)]): #ВЫВОД В ТЕКСТОВЫЙ ФАЙЛ
    f.write(x['text'])

