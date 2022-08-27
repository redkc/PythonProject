# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/8/27 9:37
# @Author : redkc02
# @File : 爬虫.百度sousou关键词.py
# @Software: PyCharm
import requests
kv = {"wd":"python"}
try:
    r = requests.get("http://www.baidu.com/s",params="wd")
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(len(r.text))
except:
    print("爬取失败")