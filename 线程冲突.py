# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/10/16 16:09
# @Author : redkc02
# @File : 线程冲突.py
# @Software: PyCharm
'''
【线程冲突】示例：
 多个线程并发访问同⼀个变量⽽互相⼲扰
'''
import threading
import time

money = 0


# CPU分配的时间⽚不⾜以完成⼀百万次加法运算，
# 因此结果还没有被保存到内存中就被其它线程所打断
def addMoney():
    global money
    for i in range(1000000):
        money += 1
        print(money)


# 创建线程锁
lock = threading.Lock()


def addMoneyWithLock():
    # print("addMoneyWithLock")
    time.sleep(1)
    global money
    # print(lock.acquire())
    # if lock.acquire():
    # for i in range(1000000):
    # money += 1
    # lock.release()
    # 独占线程锁
    with lock:  # 阻塞直到拿到线程锁
        # -----下⾯的代码只有拿到lock对象才能执⾏-----
        for i in range(1000000):
            money += 1
            # 释放线程锁，以使其它线程能够拿到并执⾏逻辑
            # ----------------锁已被释放-----------------
            print(money)


# 5条线程同时访问money变量，导致结果不正确
def conflictDemo():
    for i in range(5):
        t = threading.Thread(target=addMoney)
        t.start()


# 通过线程同步（依次执⾏）解决线程冲突
def handleConflictBySync():
    for i in range(5):
        t = threading.Thread(target=addMoney)
        t.start()
        t.join()  # ⼀直阻塞到t运⾏完毕


# 通过依次独占线程锁解决线程冲突
def handleConflictByLock():
    # 并发5条线程
    for i in range(5):
        t = threading.Thread(target=addMoneyWithLock)
        t.start()


if __name__ == '__main__':
    # conflictDemo()
    # handleConflictBySync()
    handleConflictByLock()
    pass
