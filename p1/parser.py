import requests, pymongo, re
from bs4 import BeautifulSoup
from pymongo import MongoClient, ASCENDING, DESCENDING
f = open('input.txt', 'w')
client = MongoClient()
database = client.v102news
news = database.news

source = 'https://v102.ru/'
response = requests.get(source)
sp = BeautifulSoup(response.text, 'lxml')
mainPage = sp.find('div', class_='col-lg-6 col-sm-12 col-xs-12 main')
head = mainPage.find_all('a', class_='detail-link-text')
startLink = head[0].get('href') # news/'id'.html
splitArrayOne = startLink.split('/') # 'id'.html
splitArrayTwo =  splitArrayOne[2].split('.') # 'id'
startID = splitArrayTwo[0]


for i in range(0, 40):
    
    url = "https://v102.ru/news/" + str(int(startID) - i) + ".html"#2 ссылка
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    bigline = soup.find('div', class_='short-text')
    headline = soup.find('div', class_='col-lg-11')
    newsTimes = soup.find('span', class_='date-new')
    
    headline = headline.text #` заголовок
    newsLine = bigline.text
    newsLine =  re.sub("^\s+|\n|\r|\s+$", '', newsLine) #3 текст новости
    newsTime = newsTimes.text #4   дата
    if newsTime:
        s1="".join(c for c in newsTime if c.isalpha()==False)
        newsTime = s1
    news_ = {
    "headline":headline,
    "text":newsLine,
    "url":url,
    "time":newsTime
    }
    if news.find_one({'headline': headline}) is None:
        if news.find_one({'url': url}) is None:
            if news.find_one({'time': newsTime}) is None:
                news.insert_one(news_)
                print('added entry to the database', i, url )
    else:
        print('entry already exists', i, url )
    
