import sys
import pygame
from pygame.locals import*
import random

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)

img = pygame.image.load("타코.png")
img = pygame.transform.scale(img, (25, 25))

entry = pygame.image.load("엔트리봇.png")
entry = pygame.transform.scale(entry, (35, 35))

l_size = img.get_size()
m_size = entry.get_size()

l_x = []
l_y = []

m_x, m_y = 250, 480

cnt = 0

game_over = False

while(True):
    if(game_over):
        break
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    cnt += 1
    if (cnt >= 20):
        cnt = 0
        l_x.append(random.randint(0, 500))
        l_y.append(0)
    for i in range(len(l_x)):
        l_y[i] += 5
        SCREEN.blit(img, (l_x[i], l_y[i]))
        if(l_y[i] >= 510):
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
            break
    key_event = pygame.key.get_pressed()
    if(key_event[pygame.K_LEFT]):
        if(m_x > 0):
            m_x -= 5
    if(key_event[pygame.K_RIGHT]):
        if(m_x < 465):
            m_x += 5
    SCREEN.blit(entry, (m_x, m_y))
    for i in range(len(l_x)):
        if(l_x[i] + 25 >= m_x and m_x + 35 >= l_x[i]):
            if(l_y[i] - 25 >= m_y):
                msg = sysfont.render("Game Over!", True, (255, 0, 0))
                SCREEN.blit(msg, (160, 250))
                game_over = True
                
    pygame.display.update()
    CLOCK.tick(60)
    
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
