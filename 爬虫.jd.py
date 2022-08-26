# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/8/26 22:48
# @Author : redkc02
# @File : 爬虫.jd.py
# @Software: PyCharm
import requests

url = "https://item.jd.com/100028235502.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")