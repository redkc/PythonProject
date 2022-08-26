# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/8/26 23:28
# @Author : redkc02
# @File : 爬虫.ymx.py
# @Software: PyCharm
import requests
try:
    kv = {"user-agent":"Mozilla/5.0"}
    url = "https://www.amazon.cn/dp/B0B3QSTTHX/ref=s9_acsd_hps_bw_c2_x_0_i"
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:2000])
except:
    print("爬取失败")