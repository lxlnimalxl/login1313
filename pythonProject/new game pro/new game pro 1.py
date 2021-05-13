import pygame, sys
from pygame.locals import *
pygame.init()
x = 500
y = 400
win = (800, 600)
speed = 5
w = 80
h = 80
size = 10
window = pygame.display.set_mode(win)
pygame.display.set_caption("nima game")
bg = pygame.image.load("back11.png")
BG = pygame.transform.scale(bg, (win))




while True:
    charater = pygame.image.load("car211.png")
    CHAR = pygame.transform.scale(charater, (w, h))
    window.blit(BG, (0, 0))
    window.blit(BG, (x, y))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                x += speed
            if event.key == K_a:
                x -= speed
        if event.type == KEYUP:
            if event.key == K_w:
                y -= speed
            if event.key == K_s:
                y += speed
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x -= speed
            if event.button == 3:
                x += speed
            if event.button == 4:
                w += size
                h += size
            if event.button == 5:
                w -= size
                h -= size
            if w < 0 or h < 0:
                w = 80
                h = 80
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                y += speed
            if event.key == K_UP:
                y -= speed
    pygame.display.update()
