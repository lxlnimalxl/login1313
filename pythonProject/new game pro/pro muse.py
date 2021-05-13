import pygame, sys
from pygame.locals import *
window = pygame.display.set_mode((800, 600))
x = 0
y = 0
blak = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
purple = (150, 0, 150)
yellow = (255, 255, 0)
color = red


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            x, y = event.pos
        window.fill(blak)
        pygame.draw.line(window, color, (x, 0), (x, 600), 5)
        pygame.draw.line(window, color, (0, y), (800, y), 5)
        if event.type == KEYDOWN:
            if event.key == K_r:
                color = red
            if event.key == K_g:
                color = green
            if event.key == K_p:
                color = purple
            if event.key == K_c:
                color = cyan
            if event.key == K_y:
                color = yellow
        pygame.display.update()
