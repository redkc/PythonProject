# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/10 0:00
# @Author : redkc02
# @File : demo.py
# @Software: PyCharm
import pygame
import sys
import pygame.freetype
pygame.init()
icon = pygame.image.load("R-C.png")
pygame.display.set_icon(icon)
vInfo = pygame.display.Info()
# size = width,height = vInfo.current_w,vInfo.current_h
size = width,height = 600,600
speed = [1,1]
GOLD = 255,251,0
BLACK = 0,0,0
pos = [230,160]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
# screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("pygame游戏之旅")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
f1rect = f1.render_to(screen,pos,"wangyuchao",fgcolor=GOLD,size=50)
# ball = pygame.image.load("PYG02-ball.gif")
# ballrect = ball.get_rect()
fps = 300
fclock =pygame.time.Clock()
still = False
bgcolor = pygame.Color("black")

def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0]<0 or pos[0] + f1rect.width>width:
            speed[0]=-speed[0]
    if pos[1]<0 or pos[1]+f1rect.height>height:
            speed[1]=-speed[1]
    pos[0]=pos[0]+speed[0]
    pos[1]=pos[1]+speed[1]


    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             speed[0] =speed[0] if speed[0]==0 else (abs(speed[0]-1))*int(speed[0]/abs(speed[0]))
    #         elif event.key == pygame.K_RIGHT:
    #             speed[0] =speed[0]+1 if speed[0]>0 else speed[0]-1
    #         elif event.key == pygame.K_UP:
    #             speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
    #         elif event.key == pygame.K_DOWN:
    #             speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1] - 1)) * int(speed[1] / abs(speed[1]))
    #         elif event.key == pygame.K_ESCAPE:
    #             sys.exit()
    #     elif event.type == pygame.VIDEORESIZE:
    #         size =width,height = event.size[0],event.size[1]
    #         screen =pygame.display.set_mode(size,pygame.RESIZABLE)
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             still = True
    #     elif event.type == pygame.MOUSEBUTTONUP:
    #         still = False
    #         if event.button == 1:
    #             ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
    #     elif event.type == pygame.MOUSEMOTION:
    #         if event.buttons[0]==1:
    #             ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
    # if pygame.display.get_active() and not still:
    #     ballrect = ballrect.move(speed[0],speed[1])
    # if ballrect.left<0 or ballrect.right>width:
    #     speed[0]=-speed[0]
    #     if ballrect.right>width and ballrect.right + speed[0]>ballrect.right:
    #         speed[0] = -speed[0]
    # if ballrect.top<0 or ballrect.bottom>height:
    #     speed[1]=-speed[1]
    #     if ballrect.bottom> height and ballrect.bottom + speed[1]>ballrect.bottom:
    #         speed[1] = -speed[1]
    # bgcolor.r = RGBChannel(ballrect.left*255/width)
    # bgcolor.g = RGBChannel(ballrect.top*255/height)
    # bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
    screen.fill(bgcolor)
    f1rect  =f1.render_to(screen,pos,"wangyuchao",fgcolor=GOLD,size=50)

    # screen.blit(ball,ballrect)
    fclock.tick(fps)
    pygame.display.update()