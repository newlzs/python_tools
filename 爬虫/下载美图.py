from bs4 import BeautifulSoup
import requests

URL = "http://www.ngchina.com.cn/animals/"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {'class': 'img_list'})

import os

os.makedirs('G:/桌面/img/', exist_ok=True)

for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open("G:/桌面/img/%s" % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('saved %s' % image_name)

from bs4 import BeautifulSoup
import re
import requests
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
        }
Base_URL = "https://picjumbo.com/free-stock-photos/nature/page/"
for i in range(10):
    URL = Base_URL + str(i + 1)
    html = requests.get(URL, headers=headers).text

    soup = BeautifulSoup(html, 'lxml')
    img_ul = soup.find_all('picture')
    for ul in img_ul:
        img = ul.find('img')
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open("G:/桌面/img/%s" % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        print("saved %s" % image_name)