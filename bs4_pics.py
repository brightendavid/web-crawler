# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:17:08 2021

@author: zero
"""

# bs4.pics.py
'''1. 获取主网页源代码'''
import requests
from bs4 import BeautifulSoup

# url="https://sc.chinaz.com/tupian/"
url = "http://www.jituwang.com/tuku/biology/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
resp.encoding = "utf-8"
resp_text = resp.text

'''2.从网页源代码获取子标签里的链接'''
soup = BeautifulSoup(resp_text, 'html.parser')
img_tags = soup.find_all("img")

'''3.爬取链接下的图片，并写入文件'''
for ipic in img_tags:
    href = ipic.get('src')
    img_resp = requests.get(href)
    tupian = img_resp.content
    tupian_name = href.split('/')[-1]
    with open("./image2/" + tupian_name, mode='wb')as f:
        f.write(tupian)
        f.close()
resp.close()
