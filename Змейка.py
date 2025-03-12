import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Параметры экрана
WIDTH = 600
HEIGHT = 400

# Размер блока змейки
BLOCK_SIZE = 10

# Скорость змейки
SPEED = 15

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Шрифт для отображения счета
font_style = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

def display_message(msg, color, x, y):
    message = font_style.render(msg, True, color)
    screen.blit(message, [x, y])

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            display_message("Вы проиграли! Нажмите Q для выхода или C для повтора", RED, WIDTH // 10, HEIGHT // 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

game_loop()