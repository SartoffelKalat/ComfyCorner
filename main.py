import pygame
from unit import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

hero = Unit(30, 30, 60, 60)

move_speed_hero = 3
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: hero.move_up(move_speed_hero)
    if pressed[pygame.K_DOWN]: hero.move_down(move_speed_hero)
    if pressed[pygame.K_LEFT]: hero.move_left(move_speed_hero)
    if pressed[pygame.K_RIGHT]: hero.move_right(move_speed_hero)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), hero.get_rectangle())

    pygame.display.flip()

    clock.tick(60)
