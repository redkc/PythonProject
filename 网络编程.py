# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 14:55
# @Author : redkc02
# @File : 网络编程.py
# @Software: PyCharm
import socket
# 创建socket对象
# 发起链接请求
# connect（元组）
# （host,port)ip地址和端口号需要和服务器中绑定的ip地址以及端口号保持一致
# ip_port = ("192.168.136.130",22)
# 3、发送数据
# send(string)
# close()
"""
import socket
bind(元组)，将端口号和ip地址创建元组，然后传参
（host,port)
服务端监听请求，随时准备接受客户端发来的链接
不能无限大
print("server waiting_")
4、服务端接收到客户端的请求，被动打开进行链接
accept（） 在链接的状态下，会处于阻塞状态
5、服务端接受消息
recv(size)
可以一次性接受多大的数据
6 serverSocket.close()
"""
import socket
server = socket.socket()
server.bind(("",6666))
server.listen(5)
conn,address = server.accept()
print("连接成功")
while True:

     clientData = conn.recv(1024)
     result = clientData.decode("utf-8")
     print("客户端对服务端说：",result)
     if result == "bye" or result == "再⻅":
         break
     sendData = input("请输⼊要给回复客户端的数据：")
     conn.send(sendData.encode("utf-8"))
server.close()
