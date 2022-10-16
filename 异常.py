# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 10:36
# @Author : redkc02
# @File : 异常.py
# @Software: PyCharm
list1 = [23,54,6,6]
print("over")
# NameError
# TypeError
# indexError
# keyError ValueError
# AttributeError ImportError
# SyntaxError UnboundLocalError
# 捕获异常，抛出异常
"""
try:
可能存在的异常的代码
except 错误表示码 as 变量：
语句1
else:
语句2
try-except-else 用法类似if-elif-else
else 可有可无，根据具体需求决定
try后面的代码块被称为监测区域
原理：首先执行try中的语句，如果try中的语句没有异常，则直接跳过所有的except语句，执行else；如果try
中语句异常，则去except分支中进行匹配错误码，如果匹配到了，则执行except后面的语句，如果没有except匹配，
则异常仍然没有被拦截
try-except-finally 无论异常是否匹配except ,finally语句都会被执行
rasie抛出一个指定的异常对象：nameerror 异常对象通过错误标识码创建
"""
class MyException(Exception):
    def __int__(self,msg):
        super(MyException,self).__init__()
        self.msg =msg

    def _str_(self):
        return self.msg

    def handle(self):
        print("出现了异常")

try:
    raise MyException("自己异常的类型")

except MyException as e:
        print(e)
        e.handle()

