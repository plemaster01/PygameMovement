# How to make objects move in PyGame!
import random

import pygame
pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Movement!')

timer = pygame.time.Clock()
fps = 60
player_x = 300
player_y = 300
part_one = False
part_two = False
part_three = True
player_speed = 3
x_direction = 0
y_direction = 0
world_speed = 10
obstacles = [WIDTH - 100, WIDTH + 100, WIDTH + 300]
walk_1 = pygame.transform.scale(pygame.image.load('images/walk_1.png'), (80, 120))
walk_2 = pygame.transform.scale(pygame.image.load('images/walk_1.png'), (80, 120))
idle_1 = pygame.transform.scale(pygame.image.load('images/idle_1.png'), (80, 120))
jump_1 = pygame.transform.scale(pygame.image.load('images/jump_1.png'), (80, 120))
animation_counter = 0


def draw_player():
    pygame.draw.rect(screen, 'orange', [player_x, player_y, 100, 100], 0, 5)


def draw_world():
    pygame.draw.rect(screen, 'brown', [0, HEIGHT - 100, WIDTH, 100])
    for i in range(len(obstacles)):
        pygame.draw.rect(screen, 'red', [obstacles[i], HEIGHT - 150, 40, 50])


def draw_sprite():
    global animation_counter
    pygame.draw.rect(screen, 'brown', [0, HEIGHT - 100, WIDTH, 100])
    # figure out where the sprite is on screen, and choose image accordingly
    if x_direction != 0:
        animation_counter += 1
        if animation_counter < 15:
            image = walk_1
        elif animation_counter < 30:
            image = idle_1
        elif animation_counter < 45:
            image = walk_2
        else:
            image = idle_1
        if x_direction == -1:
            image = pygame.transform.flip(image, True, False)
    else:
        image = idle_1

    if animation_counter >= 60:
        animation_counter = 0
    if player_y < HEIGHT - 220:
        image = jump_1
    screen.blit(image, (player_x, player_y))


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    if part_one or part_two:
        draw_player()
    if part_two:
        draw_world()
    if part_three:
        draw_sprite()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if part_one or part_three:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_direction = 1
                elif event.key == pygame.K_LEFT:
                    x_direction = -1
                elif event.key == pygame.K_UP:
                    y_direction = -1
                elif event.key == pygame.K_DOWN:
                    y_direction = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_direction = 0
                elif event.key == pygame.K_LEFT:
                    x_direction = 0
                elif event.key == pygame.K_UP:
                    y_direction = 0
                elif event.key == pygame.K_DOWN:
                    y_direction = 0
        elif part_two:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_direction = 1
                elif event.key == pygame.K_LEFT:
                    x_direction = -1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_direction = 0
                elif event.key == pygame.K_LEFT:
                    x_direction = 0

    if part_one or part_three:
        player_x += player_speed * x_direction
        player_y += player_speed * y_direction

    if part_two:
        for i in range(len(obstacles)):
            obstacles[i] -= world_speed * x_direction
            if obstacles[i] < -300:
                obstacles[i] = WIDTH + random.randint(0, 300)
            elif obstacles[i] > WIDTH + 300:
                obstacles[i] = random.randint(-300, 0)


    pygame.display.flip()
pygame.quit()