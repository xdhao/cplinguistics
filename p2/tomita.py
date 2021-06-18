import pymongo, os
from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient()
database = client.v102news
news = database.news
tomita = database.tomita
os.system('cd /home/vagrant/tomita-parser/build/bin/')

for x in news.find( {} ).sort([('_id', ASCENDING)]):
    finput = open('input.txt', 'w')
    finput.write(x['text'])
    finput.close()
    
    os.system('./tomita-parser config.proto')
    
    foutput = open('output.txt', 'r').readlines()
        
    for j in range(len(foutput)):
        if foutput[j].find('Person') > -1:
            if len(foutput[j-1]) > 10:
                tomita_ = {
                "text": foutput[j-1],
                "name": foutput[j+2][12:]
                }
                tomita.insert_one(tomita_)

f = open('source.txt', 'w')
for x in tomita.find( {} ).sort([('_id', ASCENDING)]):
    f.write(x['name'])
f.close()
