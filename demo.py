# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/22 18:04
# @Author : redkc02
# @File : demo.py
# @Software: PyCharm
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "这是网站主页"

@app.route('/login/')
def login():
    return '<input type="text" placeholder="请输入用户名"/> <button> 提交</button>'
app.run()