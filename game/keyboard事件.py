# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/11 14:31
# @Author : redkc02
# @File : keyboard事件.py
# @Software: PyCharm
import pygame,sys
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("pygame事件处理")
fps = 1
fclock = pygame.time.Clock()
num = 1
while True:
    uevent = pygame.event.Event(pygame.KEYDOWN,{"unicode":123,"key":pygame.K_SPACE,"MOD":pygame.KMOD_ALT})
    # pygame.event.post(uevent)
    # num +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:","#",event.key,event.mod)
            else:
                print("[KEYDOWN]:",event.unicode,event.key)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:",event.pos,event.rel,event.buttons)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:",event.pos,event.button)
    pygame.display.update()
