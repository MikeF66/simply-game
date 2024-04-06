import pygame
import random
from datetime import datetime

pygame.init()

def draw_text(surf, text, size, x, y):   #Рендерим текст
    font = pygame.font.SysFont(None, size)  # размер шрифта
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
game_paused = False  # переменная для паузы в игре

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started:
            draw_text(screen, "Для начала игры кликни мышью", 36, 200, 270)  # Отображаем надпись
            if event.type == pygame.MOUSEBUTTONDOWN:  # Старт игры после клика
                game_started = True
                start_time = datetime.now()

        elif game_started and not game_paused:
            target_x += random.randint(-10, 10)
            if target_x > SCREEN_WIDTH - target_width:
                target_x -= random.randint(0, 10)
            elif 0 < target_x < target_width:
                target_x += random.randint(0, 10)
            target_y += random.randint(-8, 10)
            if target_y > SCREEN_HEIGHT - target_height:
                target_y -= random.randint(5, 20)
            elif 0 < target_y < target_height:
                target_y += random.randint(5, 20)

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
                if total_clicks >= 20:  # условие для паузы
                    game_paused = True
                    end_time = datetime.now()  # фксирует время окончания

    if game_started and not game_paused:
        screen.blit(target_image, (target_x, target_y))
    if game_started:
        if game_paused:
            elapsed_time = end_time - start_time  # время фиксируется на момент паузы
            size = 36  # размер шрифта
            draw_text(screen, f'Вы израсходовали обойму: {total_clicks} патронов', 40, 125, 230)  # вывод выстрелов
            draw_text(screen, f'за время: {elapsed_time.seconds} секунд', 40, 253, 270)  # вывод времени
            draw_text(screen, f'и попали в цель: {hits} раз', 40, 220, 310)  #вывод попаданий
        else:
            elapsed_time = datetime.now() - start_time # если игра началась
            draw_text(screen, f'Время игры: {elapsed_time.seconds}', 24, 10, 10) #вывод времени
            draw_text(screen, f'Выстрелы: {total_clicks}', 24, 10, 25)  #вывод выстрелов
            draw_text(screen, f'Попадания: {hits}', 24, 10, 40)   #вывод попаданий

    pygame.display.update()


pygame.quit()
