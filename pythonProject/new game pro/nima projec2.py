import pygame, sys
from pygame.locals import *
a = (800, 600)
x = 0
y = 0
h = 0
w = 0
black = (0, 0, 0)
poinet = []
draw = False
draw2 = False
draw3 = False
poinet2 = []
purple = (150, 0, 150)
window = pygame.display.set_mode(a)


blue = (0, 255, 240)
#pygame.draw.line(window, blue, (60, 20), (250, 100), 1)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
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
                if len(poinet) >= 1 :
                  poinet.pop()
            if event.button == 3:
                if len(poinet2) >= 1:
                  poinet2.pop()
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 :
                draw = False
        if event.type == MOUSEMOTION and draw:
            if len(poinet) >= 2:
              poinet[-1] = event.pos
    window.fill(black)
    if len(poinet) >= 2:
        pygame.draw.lines(window, blue, False, poinet, 2)
    if len(poinet2) >= 2:
        pygame.draw.lines(window, purple, False, poinet2, 2)
    pygame.display.update()