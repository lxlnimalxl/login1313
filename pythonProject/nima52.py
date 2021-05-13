import pygame,time,sys
# اندازه صحفه

window = pygame.display.set_mode([800, 600])

#عنوان برنامه

pygame.display.set_caption("عنوان بازی")
#برای تغییر رنگ پس زمینه

#window.fill()


#رنگ های شکل ها
red =(255, 0, 0)
green =(0, 255, 0)
blue =(0, 0, 255)
white =(255, 255, 255)
black =(0, 0, 0)
yellow =(255, 255, 0)
#نحوه ساخت شکل مستطیل

pygame.draw.rect(window , red , ((400, 300), (100, 50)), 1)
#برای فعال شدن عبارت زیر را وارد کنید
#pygame.display.update()

#برای شکل دایره

# noinspection PyTypeChecker
pygame.draw.circle(window, blue, (300, 250), 20, 1)

#برای ساخت بیضی

pygame.draw.ellipse(window, white, (500, 400, 100, 50), 1)

pygame.display.update()

#برای ساخت چند ضلعی

pygame.draw.polygon(window, yellow, ((100, 50), (200, 50), (175, 100), (250, 85)))
pygame.display.update()

#ساخت شکل کمان

pygame.draw.arc(window, green, (600, 100, 50, 50), 1, 4)
pygame.display.update()

# رسم خط ها
#line
pygame.draw.line(window, red, (200, 100), (250, 150))
pygame.display.update()
#aaline
pygame.draw.aaline(window, red, (50, 100), (150, 100))
pygame.display.update()
#lines
pygame.draw.lines(window, white, False, ((300, 300), (270, 300), (250, 100)))
pygame.display.update()
#True اگه بزاری می بنده

#ساخت ایکون برای بازی

#img = pygame.image.load("icon.png")
#ygame.display.set_icon(img)
#برای گذاشتن بک گراند
#bg = pygame.image.load("icon2.jpg")
#BG = pygame.transform.scale(bg, (800, 600))
#window.blit(BG, (0, 0))
#اموزش قرار دادن عکس روی بکگراند
#img1 = pygame.image.load("icon.png")
#img1 = pygame.transform.scale(img1, (140, 120))
#window.blit(img1, (300, 200))

#فونت و متن
text = "New game"
fonte = pygame.font.Font(None, 50)

t_f = fonte.render(text, True, (yellow))
window.blit(t_f, (200, 100))




#pygame.display.update()

#مدت زمان فعال بودن صحفه

time.sleep(20)

# mine loop
#مال هر اتفاقی که در صحفه میافته رو مینویسه و تکرار حلقه

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

#فونت
#fonts = pygame.font.get_fonts()
# for f in fonts:
#    print(f)