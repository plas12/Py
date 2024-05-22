'''
import sys
import pygame
from pygame.locals import*

pygame.init()
SCREEN = pygame.display.set_mode((700, 700))
CLOCK = pygame.time.Clock()

img = pygame.image.load("금고열림1.png")

img_size = img.get_size()
print(img_size)

while(True):
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.blit(img, (0, 0))

    pygame.display.update()
    CLOCK.tick(1)


import sys
import pygame
from pygame.locals import*

pygame.init()
SCREEN = pygame.display.set_mode((300, 300))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 30)
txt = "Weit.."
txt2 = "key Down!"

while(True):
    SCREEN.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            txt = "LEFT" + txt2
        if key_event[pygame.K_RIGHT]:
            txt = "Right" + txt2
        if key_event[pygame.K_UP]:
            txt = "UP" + txt2
        if key_event[pygame.K_DOWN]:
            txt = "Down" + txt2
        if key_event[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    msg = sysfont.render(txt, True, (0, 0, 0))
    SCREEN.blit(msg, (50, 100))
    pygame.display.update()
    CLOCK.tick(60)
'''

import sys
import pygame
from pygame.locals import*
import random

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()

light_img = pygame.image.load("타코.jpg")

l_x = []
l_y = []

cnt = 0

while(True):
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.puit()
            sys.exit()
    cnt += 1
    if (cnt >= 20):
        cnt = 0
        l_x.append(random.rand(0, 600))
        l_y.apped(0)
    for i in range(len(l_x)):


    if(l_y >= 550):
        l_x.remove(l_x[i])
        l_y.remove(i_y[i])
        break
    pygame.display.update()
    CLOCK.tixk(60)
