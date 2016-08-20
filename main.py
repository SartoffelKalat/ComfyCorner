from hero import *
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

hero = Hero(30, 30, 60, 60)
last_shot = 0
move_speed_hero = 5
shot_interval_ms = 300
clock = pygame.time.Clock()
allow_shot = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    # Shooting
    if not allow_shot and (pygame.time.get_ticks() - last_shot) > shot_interval_ms:
        allow_shot = True

    if allow_shot:
        if pressed[pygame.K_UP]:
            hero.shoot_up()
        elif pressed[pygame.K_DOWN]:
            hero.shoot_down()
        elif pressed[pygame.K_LEFT]:
            hero.shoot_left()
        elif pressed[pygame.K_RIGHT]:
            hero.shoot_right()
        if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
            allow_shot = False
            last_shot = pygame.time.get_ticks()

    # Movement
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
        bullet.move_in_direction()
        pygame.draw.rect(screen, (0, 128, 255), bullet.get_rectangle())
    pygame.display.flip()

    clock.tick(60)
