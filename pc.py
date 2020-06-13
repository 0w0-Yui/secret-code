'''#\31 > div.ranking-image-item > a'''
'''#\31'''
'''#\32'''
'''#\35'''
'''
"Host": "www.pixiv.net",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.pixiv.net/ranking.php",
"Connection": "keep-alive",
"Cookie": "__cfduid=d94121b2330d2f7e273302c2f330767361590716115; first_visit_datetime_pc=2020-05-29+10%3A35%3A16; PHPSESSID=54640979_NmPfJVaKXKVTPxWnoecoio4gXY5W2kYx; p_ab_id=6; p_ab_id_2=3; p_ab_d_id=2026495101; yuid_b=EiZwmRc; __utma=235335808.1032722632.1590716139.1590716139.1590716139.1; __utmb=235335808.4.10.1590716139; __utmc=235335808; __utmz=235335808.1590716139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=54640979=1^9=p_ab_id=6=1^10=p_ab_id_2=3=1^11=lang=zh=1; __utmt=1; __tins__20061455=%7B%22sid%22%3A%201590716139593%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201590718114596%7D; __51cke__=; __51laig__=5; login_bc=1; _ga=GA1.2.1032722632.1590716139; _gid=GA1.2.403363295.1590716170; device_token=af3afa670cd77dffdbe857f4944d0a0b; privacy_policy_agreement=2; c_type=31; a_type=0; b_type=2; _fbp=fb.1.1590716195455.1242615109; login_ever=yes",
"Upgrade-Insecure-Requests": "1",
'''

import requests
import urllib
from bs4 import BeautifulSoup
import json
import time
import os
import sys
headers = {
    "Host": "www.pixiv.net",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":
    "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.pixiv.net/ranking.php",
    "Connection": "keep-alive",
    "Cookie":
    "__cfduid=d94121b2330d2f7e273302c2f330767361590716115; first_visit_datetime_pc=2020-05-29+10%3A35%3A16; PHPSESSID=54640979_NmPfJVaKXKVTPxWnoecoio4gXY5W2kYx; p_ab_id=6; p_ab_id_2=3; p_ab_d_id=2026495101; yuid_b=EiZwmRc; __utma=235335808.1032722632.1590716139.1590716139.1590716139.1; __utmb=235335808.4.10.1590716139; __utmc=235335808; __utmz=235335808.1590716139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=54640979=1^9=p_ab_id=6=1^10=p_ab_id_2=3=1^11=lang=zh=1; __utmt=1; __tins__20061455=%7B%22sid%22%3A%201590716139593%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201590718114596%7D; __51cke__=; __51laig__=5; login_bc=1; _ga=GA1.2.1032722632.1590716139; _gid=GA1.2.403363295.1590716170; device_token=af3afa670cd77dffdbe857f4944d0a0b; privacy_policy_agreement=2; c_type=31; a_type=0; b_type=2; _fbp=fb.1.1590716195455.1242615109; login_ever=yes",
    "Upgrade-Insecure-Requests": "1"
}
cookies = {
    "__51cke__": "",
    "__51laig__": "5",
    "__cfduid": "d94121b2330d2f7e273302c2f330767361590716115",
    "__tins__20061455":
    "{\"sid\": 1590716139593, \"vd\": 5, \"expires\": 1590718114596}",
    "__utma": "235335808.1032722632.1590716139.1590716139.1590716139.1",
    "__utmb": "235335808.4.10.1590716139",
    "__utmc": "235335808",
    "__utmt": "1",
    "__utmv":
    "235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=54640979=1^9=p_ab_id=6=1^10=p_ab_id_2=3=1^11=lang=zh=1",
    "__utmz":
    "235335808.1590716139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "_fbp": "fb.1.1590716195455.1242615109",
    "_ga": "GA1.2.1032722632.1590716139",
    "_gid": "GA1.2.403363295.1590716170",
    "a_type": "0",
    "b_type": "2",
    "c_type": "31",
    "device_token": "af3afa670cd77dffdbe857f4944d0a0b",
    "first_visit_datetime_pc": "2020-05-29+10:35:16",
    "login_bc": "1",
    "login_ever": "yes",
    "p_ab_d_id": "2026495101",
    "p_ab_id": "6",
    "p_ab_id_2": "3",
    "PHPSESSID": "54640979_NmPfJVaKXKVTPxWnoecoio4gXY5W2kYx",
    "privacy_policy_agreement": "2",
    "yuid_b": "EiZwmRc"
}
# http://www.pixiv.net/ranking.php?format=json&mode=daily&p=1
# http://www.pixiv.net/ranking.php?format=json&mode=daily_r18&p=1
# http://www.pixiv.net/ranking.php?format=json&mode=daily_r18g&p=1
# https://api.imjad.cn/pixiv/v2/?type=illust&id=67994735
api_list = {
    'general': 'http://www.pixiv.net/ranking.php?format=json&mode=daily&p=1',
    'r18': 'http://www.pixiv.net/ranking.php?format=json&mode=daily_r18&p=1',
    'img': 'https://api.imjad.cn/pixiv/v2/?type=illust&id='
}


def getgeneraltop(format='json'):
    response = requests.get(api_list['general'], headers=headers)
    js = json.loads(response.text)
    if format == 'json':
        return js
    elif format == 'dict':
        return toptodict(js)
    else:
        return response.text


def getadulttop(format='json'):
    response = requests.get(api_list['r18'], headers=headers, cookies=cookies)
    js = json.loads(response.text)
    if format == 'json':
        return js
    elif format == 'dict':
        return toptodict(js)
    else:
        return response.text


def toptodict(js):
    dict_l = []
    for i in range(0, 10):
        illust_id = js['contents'][i]['illust_id']
        illust_page_count = int(js['contents'][i]['illust_page_count'])
        dict_l.append({'id': illust_id, 'page_count': illust_page_count})
    return dict_l


def downloadimgs(top):
    date = time.strftime("%d%m%Y") 
    p = '{}\\output\\pixiv\\{}'.format(sys.path[0], date)
    if not os.path.exists(p):
        os.makedirs(p)
    for x in top:
        id = x['id']
        count = x['page_count']
        url = api_list['img'] + str(id)
        print('getting {} info'.format(id))
        response = requests.get(url)
        js = json.loads(response.text)
        imgurls = []
        if count == 1:
            imgurls.append(
                js['illust']['meta_single_page']['original_image_url'])
        else:
            for i in range(0, count):
                imgurls.append(
                    js['illust']['meta_pages'][i]['image_urls']['original'])
        for j in range(0, len(imgurls)):
            print('downloading image {}_{}'.format(id, str(j)))
            path = '{}\\{}_{}.jpg'.format(p, id, str(j))
            if os.path.exists(path):
                print('image {}_{} exists'.format(id, str(j)))
                continue
            else:
                try:
                    response = requests.get(imgurls[j],
                                            headers=headers,
                                            cookies=cookies)
                    with open(path, 'wb') as f:
                        f.write(response.content)
                except Exception as e:
                    print(e)


print(
    '============================================================================='
)
print('program started')
print('starting collect info...')
print('get adult top info')
adult = getadulttop(format='dict')
print('downloading adult top')
downloadimgs(adult)
print(
    '============================================================================='
)
print('get general top info')
general = getgeneraltop(format='dict')
print('downloading general top')
downloadimgs(general)
print(
    '============================================================================='
)
print('exit in 5 seconds...')
time.sleep(5)
