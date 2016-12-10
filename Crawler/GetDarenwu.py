#coding:utf-8
import requests,pymongo,time
from bs4 import BeautifulSoup
client = pymongo.MongoClient('localhost',27017)
daren = client['daren']
info = daren['link']
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    }
def Get_link(num):
    url = 'http://www.damanwoo.com/design?page={}'
    web_data = requests.get(url.format(str(num)),headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text,'lxml')
    link = soup.select('#content-area > section > div > div > div.post-image.clearfix > a')
    img = soup.select('#content-area > section > div > div > div.post-image.clearfix > a img')
    for links, imgs in zip(link,img):
        data = {'Link':'http://www.damanwoo.com'+ links.get('href'),'Img':imgs.get('src')}
        count = info.find({'Link':'http://www.damanwoo.com'+ links.get('href')}).count()
        if count <= 0:
            info.insert_one(data)
            print('新增一条记录！')
        else:
            print('该条记录已存在！')
def Load_info(link):
    web_data = requests.get(link,headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text,'lxml')
    title = soup.select('div.node-inner > header > h2 a')
    context = soup.select('div.content.clearfix > p')
    for i in context:
        print(i)

if __name__=='__main__':
    Load_infos = info.find().limit(1)
    for item in Load_infos:
        Load_info(item['Link'])
