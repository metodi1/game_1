import random

import pygame
from pygame import event

pygame.init()
display_width = 400
display_height = 400
sneak_block = 10
display_game = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()


def game():
    game_over = False
    snake_speed = 3
    x1 = 0
    y1 = 0

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, display_width - sneak_block) / 10) * 10
    foody = round(random.randrange(0, display_width - sneak_block) / 10) * 10

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
        pygame.draw.rect(display_game, blue, [x1, y1, sneak_block, sneak_block])
        pygame.draw.rect(display_game, red, [foodx, foody, sneak_block, sneak_block])
        if x1 == foodx and y1 == foody:
            print('Изядено')
            foodx = round(random.randrange(0, display_width - sneak_block) / 10) * 10
            foody = round(random.randrange(0, display_width - sneak_block) / 10) * 10
            snake_speed += 1
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
