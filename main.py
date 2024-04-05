import pygame
import random
from datetime import datetime

pygame.init()

total_clicks = 0   # начальные условия - кликов 0
hits = 0           # попаданий 0
game_started = False
start_time = None

font = pygame.font.SysFont(None, 24) # размер шрифта

def draw_text(surf, text, size, x, y):   #Рендерим текст
    text_surface = font.render(text, True, (255, 255, 255))  # Белый цвет текста
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ТИР")

photo = pygame.image.load("img/tir-risunok.jpg")
pygame.display.set_icon(photo)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))

total_clicks = 0 # начальные условия: выстрелы=0, попадания=0, время=0
hits = 0
game_started = False
start_time = None

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True
                start_time = datetime.now()

            total_clicks += 1  # подсчет кликов
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1  # подсчет попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))

    if game_started:
        elapsed_time = datetime.now() - start_time # если игра началась
        draw_text(screen, f'Время игры: {elapsed_time.seconds}', 18, 10, 10) #вывод времени
    draw_text(screen, f'Выстрелы: {total_clicks}', 18, 10, 25)  #вывод выстрелов
    draw_text(screen, f'Попадания: {hits}', 18, 10, 40)   #вывод попаданий

    pygame.display.update()

pygame.quit()
