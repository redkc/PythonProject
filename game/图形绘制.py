# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/11 15:42
# @Author : redkc02
# @File : 图形绘制.py
# @Software: PyCharm
import pygame ,sys
import pygame.freetype
from math import pi

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("python图形绘制")
GOLD = 255,251,0
RED = pygame.Color("red")
WHITE = 255,255,255
GREEN = pygame.Color('green')
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
# f1rect= f1.render_to(screen,(200,160),"中国和平",fgcolor=GOLD,size=50)
f1surf,f1rect = f1.render("世界和平",fgcolor=GOLD,size=50)
# r1rect = pygame.draw.rect(screen,GOLD,(100,100,200,100),5)
# 2rect = pygame.draw.rect(screen,RED,(210,210,200,100),0)
# e1rect = pygame.draw.ellipse(screen,GREEN,(50,50,500,300),3)
# c1rect = pygame.draw.circle(screen,GOLD,(200,180),30,5)
# c2rect = pygame.draw.circle(screen,GOLD,(400,180),30)
# r1rect = pygame.draw.rect(screen,RED,(170,130,60,10),3)
# r2rect = pygame.draw.rect(screen,RED,(370,130,60,10))
# plist = [(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]
# l1rect = pygame.draw.lines(screen,GOLD,True,plist,2)
# alrect = pygame.draw.arc(screen,RED,(200,220,200,100),1.4*pi,1.9*pi,3)
while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f1surf,(200,160))
    pygame.display.update()
