# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 15:26
# @Author : redkc02
# @File : client.py
# @Software: PyCharm
import socket
client = socket.socket()
client.connect(("127.0.0.1",6666))
while True:
     sendData = input("请输⼊要发送给服务端的数据：")
     client.send(sendData.encode("utf-8"))
     serverData = client.recv(1024)
     result = serverData.decode("utf-8")
     print("服务端回复：",result)
     if result == "bye":
        break
client.close()