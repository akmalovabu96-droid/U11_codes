# Iloncha SSSsssSSS (xavotir olmang, o'yinning o'zida tovushi chiqmaydi)

# kutubxonalarni import qilish
import pygame
import time
import random

# Ilon tezligi
snake_speed = 15

# Oyna o'lchami
window_x = 720
window_y = 480

# ranglarni aniqlash
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Pygame'ni ishga tushirish
pygame.init()

# O'yin oynasini sozlash
pygame.display.set_caption('Iloncha') # nomi
game_window = pygame.display.set_mode((window_x, window_y))

# FPS boshqaruvi
fps = pygame.time.Clock()

# standart joylashuvini aniqlash
snake_position = [100, 50]

# ilonning to'rta tana qismini o'rnatish
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
# meva pozitsiyasi
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# ilonning yo'nalishini o'rnatish
# o'ngga
direction = 'RIGHT'
change_to = direction

# boshlang'ich ball
score = 0

# Ballar funksiyasini ekranga chiqarish
def show_score(choice, color, font, size):
    # shrift obyektini kiritamiz
    score_font = pygame.font.SysFont(font, size)

    # yuqori chap burchakda hisoblagichni joylashtiramiz
    # score_surface
    score_surface = score_font.render('Ball hisoblagichi : ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    # matnni ko'rsatish
    game_window.blit(score_surface, score_rect)


# o'yinning yakunlanish funksiyasi
def game_over():
    # berilgan funksiya uchun shrift
    my_font = pygame.font.SysFont('times new roman', 50)

    # matn chizilishi uchun yuzasini
    # yaratish
    game_over_surface = my_font.render('Yakuniy ballingiz : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    # matnning pozitsiyasini o'rnatish
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit matnni ekranga chiqaradi
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # 2 soniyadan keyin dastur
    # yopiladi
    time.sleep(2)

    # pygame kutubxonasini faolsizlashtirish
    pygame.quit()

    # dasturdan chiqish
    quit()


# Asosiy Funksiya (O'yin boshlanishi)
while True:
    # asosiy tugmachalar harakatini boshqarish
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Agar ikkita tugma bir vaqtning o'zida bosilsa
    # Ilonning ikki tomonga harakatlanishini oldini olamiz
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Ilonni harakatlantirish
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Ilon tanasining kattalashishi mexanizmi
    # Agar mevalar va ilon to'qnashsa, ballar 10ga oshiriladi
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # O'yin tugashi uchun shartlar
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Ilon ekranning burchaklariga teginsa, (boshqatdan boshlaysiz endi, yana nima ham bo'lardi)
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Ballarni doimiy ravishda ko'rsatish
    show_score(1, white, 'times new roman', 20)

    # O'yin ekranini yangilash
    pygame.display.update()

    # Soniyasiga kadr / Yangilash tezligi
    fps.tick(snake_speed)

