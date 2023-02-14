import dis
import random

import pygame
from pygame import event

pygame.init()

pygame.display.set_caption('Snake game first trail')
display_width = 400
display_height = 400
snake_block = 10
food_block = snake_block
display_game = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

clock = pygame.time.Clock()

score_font = pygame.font.SysFont("cosmeticians", 25)


def my_snake(snake_list, snake_block):
    for x in snake_list:
        pygame.draw.rect(display_game, blue, [x[0], x[1], snake_block, snake_block])


def def_game_close(game_close, snake_lenght):
    while game_close == True:
        display_game.fill(blue)
        value = score_font.render("Your Score: " + str(snake_lenght - 1), True, red)
        value1 = score_font.render("Press A-Play Again or Q-Quit", True, red)
        display_game.blit(value, [0, 0])
        display_game.blit(value1, [0, 100])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game()
                if event.key == pygame.K_q:
                    game_close = False
                    return True


def game():
    game_over = False
    game_close = False
    snake_speed = 3
    snake_lenght = 1
    x1 = 0
    y1 = 0

    x1_change = 0
    y1_change = 0
    snake_list = []

    foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, display_width - snake_block) / 10) * 10

    event_key_previous = 0

    while not game_over:
        game_over = def_game_close(game_close, snake_lenght)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event_key_previous != event.key:
                event_key_previous = event.key
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
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display_game.fill(white)

        pygame.draw.rect(display_game, red, [foodx, foody, food_block, food_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_lenght:
            del snake_list[0]

        # ако се върне назад умира
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        # рисува змията
        my_snake(snake_list, snake_block)

        # Изяжда храната
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, display_width - snake_block) / 10) * 10
            snake_speed += 1
            snake_lenght += 1

        value = score_font.render("Your Score: " + str(snake_lenght - 1), True, green)
        display_game.blit(value, [0, 0])

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
