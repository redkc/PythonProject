# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/7 17:41
# @Author : redkc02
# @File : 正则表达式.py
# @Software: PyCharm
import re
# ls = re.findall(r'[1-9]\d{5}','BIT1000081 TSU100084')
# print(ls)
# l = re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
# print(l)
for m in re.finditer(r'[1-9]\d{5}','BIT1000081 TSU100084'):
    if m:
        print(m.group(0))
