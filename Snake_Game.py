import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set screen width and height
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    text = font.render(msg, True, color)
    screen.blit(text, [x, y])

def gameLoop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    dx, dy = 0, 0
    snake_list = []
    length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10

    while not game_over:
        while game_close:
            screen.fill(black)
            message("Game Over! Press Q-Quit or C-Play Again", red, 100, 150)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(black)
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])
        snake_list.append([x, y])

        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == [x, y]:
                game_close = True

        for pos in snake_list:
            pygame.draw.rect(screen, blue, [pos[0], pos[1], snake_block, snake_block])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
