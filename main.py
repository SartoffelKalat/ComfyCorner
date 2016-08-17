from hero import *
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

hero = Hero(30, 30, 60, 60)

move_speed_hero = 5
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        hero.shoot_up()
    if pressed[pygame.K_w] and pressed[pygame.K_a]:
        hero.move_up_left(move_speed_hero)
    elif pressed[pygame.K_w] and pressed[pygame.K_d]:
        hero.move_up_right(move_speed_hero)
    elif pressed[pygame.K_s] and pressed[pygame.K_a]:
        hero.move_down_left(move_speed_hero)
    elif pressed[pygame.K_s] and pressed[pygame.K_d]:
        hero.move_down_right(move_speed_hero)
    elif pressed[pygame.K_w]:
        hero.move_up(move_speed_hero)
    elif pressed[pygame.K_s]:
        hero.move_down(move_speed_hero)
    elif pressed[pygame.K_a]:
        hero.move_left(move_speed_hero)
    elif pressed[pygame.K_d]:
        hero.move_right(move_speed_hero)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), hero.get_rectangle())
    for bullet in hero.all_bullets:
        bullet.y += 1
        pygame.draw.rect(screen, (0, 128, 255), bullet)
    pygame.display.flip()

    clock.tick(60)
