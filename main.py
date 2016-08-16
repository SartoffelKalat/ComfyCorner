import pygame
from unit import *

pygame.init()
screen = pygame.display.set_mode((600, 300))
done = False

hero = Unit(30, 30, 60, 60)

move_speed_hero = 3
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_W]: hero.move_up(move_speed_hero)
    if pressed[pygame.K_S]: hero.move_down(move_speed_hero)
    if pressed[pygame.K_A]: hero.move_left(move_speed_hero)
    if pressed[pygame.K_D]: hero.move_right(move_speed_hero)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), hero.get_rectangle())

    pygame.display.flip()

    clock.tick(60)
