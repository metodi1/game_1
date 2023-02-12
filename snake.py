import random

import pygame
from pygame import event

pygame.init()

pygame.display.set_caption('Snake game first trail')
display_width = 400
display_height = 400
snake_block = 10
display_game = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()


def my_snake(snake_list, snake_block):
    for x in snake_list:
        pygame.draw.rect(display_game, blue, [x[0], x[1], snake_block, snake_block])


def game():
    game_over = False
    snake_speed = 3
    snake_lenght = 1
    x1 = 0
    y1 = 0

    x1_change = 0
    y1_change = 0
    snake_list = []
    foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, display_width - snake_block) / 10) * 10

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change += 10
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change -= 10
                if event.key == pygame.K_RIGHT:
                    x1_change += 10
                    y1_change = 0

                if event.key == pygame.K_LEFT:
                    x1_change -= 10
                    y1_change = 0

        if y1 > display_height or y1 < 0 or x1 < 0 or x1 > display_width:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        display_game.fill(white)

        pygame.draw.rect(display_game, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_lenght:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        my_snake(snake_list, snake_block)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, display_width - snake_block) / 10) * 10
            snake_speed += 1
            snake_lenght += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
