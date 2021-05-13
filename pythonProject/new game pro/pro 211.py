import pygame, sys, random, time
from pygame.locals import *
win = (800, 600)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
purple = (150, 0, 150)
yellow = (255, 255, 0)
p_pos = [370, 500]
e_pos =[random.randint(0, 740), 0]
enemy_l = [e_pos]
speed = 10
speed_e = 5
fps = 60
game_over = False
score = 0
font = pygame.font.Font("B Morvarid.ttf", 40)
font2 = pygame.font.Font("B Morvarid.ttf", 80)
stop = False
#music1 = pygame.mixer.Sound("Sepehr Khalse Ft PCD Ft Arta - Diklofenak.mp3")
#music1.play()



window = pygame.display.set_mode(win)
pygame.display.set_caption("simplegame")
colok = pygame.time.Clock()
def collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if p_x <= e_x < (p_x + 60) or (e_x <= p_x < (e_x + 60)):
        if p_y <= e_y < (e_y + 60) or (e_x <= p_y < (e_y + 60)):
            return True
    else:
        return False



def enemies(enemy_list):
    a = random.randint(0, 10)
    if len(enemy_list) <= 10 and a < 1:
        x_pos = random.randint(0, 740)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemise(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(window, yellow, (enemy[0], enemy[1], 60, 60))

def enemy_pos_update(enemy_list, score):
    for index, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= 600:
             enemy_pos[1] += speed_e
        else:
            enemy_list.pop(index)
            score += 1
    return score



def level(scr, spd):
    if scr <= 10:
        spd = 2
    elif scr <= 20:
        spd = 4
    elif scr <= 50:
        spd = 6
    elif scr <= 100:
        spd =8
    else:
        spd = 10
    return spd




def check_collision(enemy_list, player_pos):
    for enemy in enemy_list:
        if collision(enemy, player_pos):
            return True
    return False



def stop_function(stp):
    while stp:
        font4 = pygame.font.Font(None, 80)
        text_surface = font4.render("PAUSE", True, cyan)
        window.blit(text_surface, (300, 250))
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evt.type == KEYDOWN:
                if event.key == K_SPACE:
                    stp = False
        pygame.display.update()





def game_opening():
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("3", True, green)
    window.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    window.fill(black)
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("2", True, green)
    window.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    window.fill(black)
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("1", True, green)
    window.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    window.fill(black)
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("GO", True, green)
    window.blit(text_s, (150, 150))
    pygame.display.update()
    time.sleep(1)
    window.fill(black)

game_opening()
game_sound = pygame.mixer.music.load("Sepehr Khalse Ft PCD Ft Arta - Diklofenak.mp3")
pygame.mixer.music.play(-1)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                p_pos[0] += speed
            if event.key == K_LEFT:
                p_pos[0] -= speed
            if event.key == K_SPACE:
                stop = True
                stop_function(stop)
    #if collision(p_pos, e_pos):
    #    game_over = True
    #   break
    if check_collision(enemy_l, p_pos):
        game_over_sound = pygame.mixer.music.load("Sound 2 bad az bakht")
        pygame.mixer.music.play()
        t_s2 = font2.render("GAME OVER", True, red)
        window.blit(t_s2, (270, 270))
        t_s = font.render("your score is : " + str(score), True, (red))
        window.blit(t_s, (270, 320))
        pygame.display.update()
        time.sleep(3)
        game_over = True
        break
    if p_pos[0] <= 0:
        p_pos[0] = 0
    if p_pos[0] >= 700:
        p_pos[0] = 740
    #e_pos[1] += speed_e
    #if e_pos[1] == 600:
    #    e_pos[1] = 0
    #if (e_pos[1] >= 0) and (e_pos[1] <= 600):
     #   e_pos[1] += speed_e
    #else:
     #   e_pos[1] = 0
      #  e_pos[0] = random.randint(0, 740)
    window.fill(black)
    enemies(enemy_l)
    draw_enemise(enemy_l)
    score = enemy_pos_update(enemy_l, score)
    print(score)
    t_s = font.render("score : " + str(score), True, (red))
    window.blit(t_s, (20, 20))
    speed_e = level(score, speed_e)
    pygame.draw.rect(window, cyan, (p_pos[0], p_pos[1], 60, 60))
    colok.tick(fps)
    pygame.display.update()