import pygame, sys, random, time
from pygame.locals import *
pygame.init()
h_w = (800, 600)
color1 = (0, 0, 0)
color2 = (30, 20, 10)
color3 = (80, 50, 60)
color4 = (80, 180, 120)
color5 = (150, 150, 150)
color6 = (120, 250, 20)
color7 = (180, 130, 220)
color8 = (150, 50, 100)
color9 = (230, 140, 120)
fps = 10
worm_x = 380
worm_y = 280
speed_worm_x = 0
speed_worm_y = 0
food_x = random.randrange(0, 780, 20)
food_y = random.randrange(0, 550, 20)
win = pygame.display.set_mode(h_w)
pygame.display.set_caption("GAME_SIS_MAR")
clock = pygame.time.Clock()
worm_list = []
worm_length = 0
game_over = False
a = ["r", "l", "u", "d"]
score = 0
font = pygame.font.Font(None, 40)
scr = 0
bomb_x = random.randrange(0, 780, 20)
bomb_y = random.randrange(0, 550, 20)


def worm_function(worm_lst, wrm_x, wrm_y):
    g_over = False
    worm_head = [worm_x, worm_y]
    worm_lst.append(worm_head)
    for lst in worm_lst:
        pygame.draw.rect(win, color6, (lst[0], lst[1], 20, 20))
    for each_section in worm_lst[:-1]:
        if each_section == worm_head:
            g_over = True
    return g_over

def bomb(bom_x, bom_y):
    img1 = pygame.image.load("b1.jpg")
    IMG1 = pygame.transform.scale(img1, (20, 20))
    win.blit(IMG1, (bom_x, bom_y))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and "r" in a:
                speed_worm_x = 20
                speed_worm_y = 0
                a.clear()
                a.append("r")
                a.append("u")
                a.append("d")
            if event.key == K_LEFT and "l" in a:
                speed_worm_x = -20
                speed_worm_y = 0
                a.clear()
                a.append("l")
                a.append("u")
                a.append("d")
            elif event.key == K_DOWN and "d" in a:
                speed_worm_y = 20
                speed_worm_x = 0
                a.clear()
                a.append("r")
                a.append("d")
                a.append("l")
            elif event.key == K_UP and "u" in a:
                speed_worm_y = -20
                speed_worm_x = 0
                a.clear()
                a.append("r")
                a.append("l")
                a.append("u")
    win.fill(color4)
    if worm_function(worm_list, worm_x, worm_y):
        game_over = True
    worm_x += speed_worm_x
    worm_y += speed_worm_y
    if worm_x < 0:
        worm_x = 780
    if worm_x > 780:
        worm_x = 0
    if worm_y < 0:
        worm_y = 580
    if worm_y > 580:
        worm_y = 0
    if score % 6 != 5:
        if worm_x == food_x and worm_y == food_y:
            bomb_x = random.randrange(0, 780, 20)
            bomb_y = random.randrange(0, 550, 20)
            food_x = random.randrange(0, 780, 20)
            food_y = random.randrange(0, 580, 20)
            worm_length += 1
            scr += 1
            score += 1
    if score % 6 == 5:
        if worm_x <= food_x + 20 <= worm_x + 20:
            if worm_y <= food_y + 20 <= worm_y + 20:
                bomb_x = random.randrange(0, 780, 20)
                bomb_y = random.randrange(0, 550, 20)
                food_x = random.randrange(0, 780, 20)
                food_y = random.randrange(0, 580, 20)
                worm_length += 1
                scr += 5
                score += 1
    if bomb_x == worm_x and bomb_y == worm_y:
        img2 = pygame.image.load("b2.jpg")
        IMG2 = pygame.transform.scale(img2, (100, 100))
        win.fill(color4)
        win.blit(IMG2, (bomb_x - 50, bomb_y - 50))
        music = pygame.mixer.music.load("big_explosion_sfx_3.mp3")
        pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(2)
        game_over = True
    if len(worm_list) > worm_length:
        worm_list.pop(0)
    if score % 5 != 0 or score == 0:
        pygame.draw.rect(win, color7, (food_x, food_y, 20, 20))
    if score % 5 == 0 and score != 0:
        pygame.draw.rect(win, color7, (food_x, food_y, 40, 40))
    t_s = font.render("score : " + str(scr), True, (0, 255, 255))
    win.blit(t_s, (30, 30))
    bomb(bomb_x, bomb_y)
    pygame.display.update()
    clock.tick(fps)