'''
import sys
import pygame
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Tick Tock Timer")

CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None, 36)

timer = 0

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    timer += 1

    screen.fill((255, 255, 255))

    cnt_txt = sysfont.render("Timer : %d" % timer, True, (0, 0, 0))

    screen.blit(cnt_txt, (140, 140))

    pygame.display.update()

    CLOCK.tick(1)


import sys
import pygame
from pygame.locals import*
import random
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Tick tock, Timer")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)
cnt_txt = sysfont.render("Hi!", True, (0, 0, 0))
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(cnt_txt, (random.randint(1, 300), random.randint(1, 300)))
    pygame.display.update()
    CLOCK.tick(1)


import sys
import pygame
from pygame.locals import*
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clrs = [BLACK, RED, GREEN, BLUE]

while(True):
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    cnt_txt = sysfont.render("HELLO! PYTHON!", True, clrs[random.randint(0, 3)])
    screen.blit(cnt_txt,(80, 140))
    pygame.display.update()
    CLOCK.tick(3)


import sys
import pygame
from pygame.locals import*
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)
    rec = Rect(20, 10, 60, 40)
    pygame.draw.rect(SURFACE, RED, rec)
    pygame.draw.circle(SURFACE, GREEN, (120, 50), 10)
    pygame.draw.polygon(SURFACE, BLUE, [[50, 50], [0, 100], [100, 100]])
    pygame.draw.line(SURFACE, BLACK, [120, 0], [120, 100])
    pygame.display.update()
    CLOCK.tick(1)
'''

import sys
import pygame
from pygame.locals import*
pygame.init()
SURFACE = pygame.display.set_mode((300, 300))
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 102, 0)
BLUE = (0, 0, 153)

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)
    rec = Rect(20, 10, 60, 40)
    pygame.draw.circle(SURFACE, GREEN, (150, 150), 150)
    a = Rect(44, 44, 211, 211)
    pygame.draw.rect(SURFACE, BLUE, a)
    b = Rect(100, 100, 100, 100)
    pygame.draw.rect(SURFACE, BLACK, b)
    pygame.draw.polygon(SURFACE, RED, [[100, 100], [100, 200], [200, 200]])
    pygame.display.update()
    CLOCK.tick(1)
