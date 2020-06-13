import requests
from bs4 import BeautifulSoup
import urllib
import os
import sys
import time

fullpath = '{}\\output'.format(sys.path[0])
if not os.path.exists(fullpath):
    os.mkdir(fullpath)
host = 'https://zh.nyahentai.pro'
print('getting resourse...')
response = requests.get('https://zh.nyahentai.pro/rank/popular')
soup = BeautifulSoup(response.text, 'html.parser')
ids = []
urls = []
pages = []
i = 1
print('getting top 5 info...')
con=False
# start claim info
while len(urls) < 5:
    selector = '#content > div.container.index-container > div:nth-child('+str(
        i)+') > a'
    data = soup.select(selector+' > img')
    href = soup.select(selector)
    for item in data:
        lang = item.get('alt')
        src = item.get('data-src')
        if lang.find('中国') != -1:
            for x in href:
                a_href = x.get('href')
                p = '{}\\{}'.format(fullpath, a_href.replace(
                    '/g/', '').replace('/', ''))
                if os.path.exists(p):
                    con=True
                con=False
                pages.append(a_href)
            # pages.append(a_href.get('href'))
            if con==True:
                continue
            urls.append(src)
    i += 1
# some prepare working
print('',end='')
for i in range(0, len(pages)):
    ids.append(pages[i].replace('/g/', '').replace('/', ''))
    url = host+pages[i]
    print('getting pages info...')
    response = requests.get(host+pages[i])
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.select('#info > div:nth-child(3)')
    print(data[0].contents[0])
    pages[i] = int(data[0].contents[0].replace('共 ', '').replace(' 頁', ''))
    if pages[i] > 50:
        pages[i] = 50
    urls[i] = urls[i].replace('t.nyahentai.net', 'i.nyahentai.net')
# start downloading
for i in range(0, len(urls)):
    path = '{}\\{}'.format(fullpath, ids[i])
    os.mkdir(path)
    print('downloading {}'.format(ids[i]))
    for j in range(1, pages[i]):
        url = urls[i].replace('thumb', str(j))
        print('downloading page {} form {}'.format(j, url))
        try:
            urllib.request.urlretrieve(url, '{}\\{}.jpg'.format(path, str(j)))
        except Exception as e:
            print(e)
    print('download complete!')
print('exit in 5 seconds...')
time.sleep(5)
