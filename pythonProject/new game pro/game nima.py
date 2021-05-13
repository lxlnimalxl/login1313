import pygame, sys
from pygame.locals import *
win = (800, 600)
window = pygame.display.set_mode(win)
pygame.display.set_caption("nima draw game")
x = 0
y = 0
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
purple = (150, 0, 150)
yellow = (255, 255, 0)
color = red
a = (800, 600)
h = 0
w = 0
poinet = []
draw = False
draw2 = False
draw3 = False
poinet2 = []
purple = (150, 0, 150)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            x, y = event.pos
        window.fill(black)
        pygame.draw.line(window, color, (x, 0), (x, 600), 2)
        pygame.draw.line(window, color, (0, y), (800, y), 2)
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
        if event.type == KEYDOWN:
            if event.key == K_1:
                draw2 = True
                draw3 = False
            if event.key == K_2:
                draw2 = False
                draw3 = True
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and draw2:
                position = event.pos
                poinet += [position]
                draw = True
            if event.button == 1 and draw3:
                position = event.pos
                poinet2 += [position]
                print(poinet)
            if event.button == 3:
                if len(poinet) >= 1:
                    poinet2.pop()
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                draw = False
        if event.type == MOUSEMOTION and draw:
            if len(poinet) >= 2:
                poinet[-1] = event.pos
    if len(poinet) >= 2:
        pygame.draw.lines(window, cyan, False, poinet, 2)
    if len(poinet2) >= 2:
        pygame.draw.lines(window, yellow, False, poinet2, 2)
        pygame.display.update()