# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 15:59
# @Author : redkc02
# @File : 多线程.py
# @Software: PyCharm
import  multiprocessing
import  threading
import time
import os
# 子线程需要做的事
def doSth(arg):
 # 拿到当前线程的名称和线程号id
   threadName = threading.current_thread().getName()
   tid = threading.current_thread().ident
   for i in range(5):
      print("%s *%d @%s,tid=%d" % (arg, i, threadName, tid))
      time.sleep(2)
# # 实现子线程
# def threadingThread():
#   t = threading.Thread(target=doSth, args=("参数⼀",)) # args=(,) 必须是元组
#   # t.setDaemon(True) # 设置为守护线程
#   t.start()

# class MyThread(threading.Thread):
#
#   def __init__(self, name, task, subtask):
#    super().__init__()
#
#    self.name = name  # 覆盖了⽗类的name
#    self.task = task  # MyThread⾃⼰的属性
#    self.subtask = subtask  # MyThread⾃⼰的属性
#
#   # 覆写⽗类的run⽅法，
#   # run⽅法以内为【要跑在⼦线程内的业务逻辑】(thread.start()会触发的业务逻辑)
#   def run(self):
#    for i in range(5):
#     print("【%s】并【%s】 *%d @%s" % (self.task, self.subtask, i,
#                                  threading.current_thread().getName()))
#
#   time.sleep(2)
#
#
# def classThread():
#   mt = MyThread("线程1", "上课", "写笔记")
#   mt.start()  # 启动线程
def importantAPI():
  print(threading.currentThread()) # 返回当前的线程变量
  # 创建五条⼦线程
  t1 = threading.Thread(target=doSth, args=("线程1",))
  t2 = threading.Thread(target=doSth, args=("线程2",))
  t3 = threading.Thread(target=doSth, args=("线程3",))
  t1.start() # 开启线程
  t2.start()
  t3.start()
  print(t1.isAlive()) # 返回线程是否活动的
  print(t2.isDaemon()) # 是否是守护线程
  print(t3.getName()) # 返回线程名
  t3.setName("巡⻦") # 设置线程名
  print(t3.getName())
  print(t3.ident) # 返回线程号
  # 返回正在运⾏的线程数量（在数值上等于len(tlist)）
  count = threading.active_count()
  print("当前活动线程有%d条" % (count))