import pygame, sys

pygame.init()

win = (800, 700)
window = pygame.display.set_mode(win)
pygame.display.set_caption("nima game")
color1 =(245, 220, 120)
color2 =(145, 190, 244)
color3 =(235, 212, 230)
x = 350
y = 500
speed = 1
celok = pygame.time.Clock()
fps = 220
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(color1)
    pygame.draw.rect(window, color2, (x, y, 100, 100))
    if (x >= 0) and (y == 500):
        x += speed
    if (y <= 500) and (x == 700):
        y -= speed
    if (x <= 700) and (y == 0):
        x -= speed
    if (y >= 0) and (x == 0):
        y += speed
    pygame.display.update()
    celok.tick(fps)