# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/8/27 9:51
# @Author : redkc02
# @File : 爬虫.图片.py
# @Software: PyCharm
import requests

path = "C:/Users/redkc02/Desktop/PythonProject/abc.jpg"
url = "https://ts1.cn.mm.bing.net/th/id/R-C.0e4bea43ecc474230d88ef73d4e99e82?rik=Uaf3iXNMPkQOaQ&riu=http%3a%2f%2fimg.mm4000.com%2ffile%2f0%2f4e%2f0713475320.jpg&ehk=BiFlSz%2fIz62YbBxZ3WH87dt8RhqKsb%2f2YE%2fCZxDtzkM%3d&risl=&pid=ImgRaw&r=0"
r = requests.get(url)
r.status_code
with open(path,'wb') as f:
    f.write(r.content)
f.close()