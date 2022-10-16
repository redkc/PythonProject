# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 10:58
# @Author : redkc02
# @File : 多任务.py
# @Software: PyCharm
import multiprocessing
import time
"""
死锁：一个资源多次调用，而多次调用都未能释放该资源就会造成一种互相等待的现象，
互斥锁
创建锁
lock = treading.Lock()
锁定
lock.acquire()
释放
lock.release()
同步是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，知道收到返回信息
才继续执行下去。
异步是指进程不需要一直等下去，二十继续执行下面操作，不管其他进程的状态，当有消息返回时系统会通知进行处理，
提高执行效率。
比如：打电话是同步，发短信是异步。
多线程和多进程：
对于计算密集型应用，应该使用多进程，可以使用多个cpu，缺点是占用资源多；
对于io密集型应用，使用多线程，线程创建开销比进程创建开销少的多。
"""
# def func(arg):
#      pname = multiprocessing.current_process().name
#      pid = multiprocessing.current_process().pid
#      print("当前进程ID=%d,name=%s" % (pid, pname))
#      for i in range(5):
#          print(arg)
#          time.sleep(1)
# if __name__ == "__main__":
#      p = multiprocessing.Process(target=func, args=("hello",))
#      # p.daemon = True # 设为【守护进程】（随主进程的结束⽽结束）
#      p.start()
#      while True:
#          print("⼦进程是否活着？", p.is_alive())
#          time.sleep(1)
#      print("main over")
import os
class MyProcess(multiprocessing.Process):
     def __init__(self, name, url):
         super().__init__()
         self.name = name
         self.url = url

     def run(self):
         pid = os.getpid()
         ppid = os.getppid()
         pname = multiprocessing.current_process().name
         print("当前进程name：", pname)
         print("当前进程id：", pid)
         print("当前进程的⽗进程id：", ppid)
if __name__ == '__main__':
 # 创建3个进程
     MyProcess("⼩分队1", "").start()
     MyProcess("⼩分队2", "").start()
     MyProcess("⼩分队3", "").start()
     print("主进程ID：", multiprocessing.current_process().pid)
     # CPU核数
     coreCount = multiprocessing.cpu_count()
     print("我的CPU是%d核的" % coreCount)