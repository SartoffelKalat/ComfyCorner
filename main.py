from hero import *
import pygame

pygame.init()

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False

hero = Hero(30, 30)
last_shot = 0

shot_interval_ms = 300
clock = pygame.time.Clock()
allow_shot = True
elapsed = 0.


def update_move_speed(delta_frames):
    hero.move_speed = hero.base_speed*delta_frames
    for bullet in hero.all_bullets:
        bullet.move_speed = bullet.base_speed * delta_frames

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    elapsed = clock.tick(144)
    delta_frames = elapsed / 1000.0
    update_move_speed(delta_frames)
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
    print(hero.get_y())
    if pressed[pygame.K_w] and pressed[pygame.K_a]:
        if hero.get_y() < 0 and hero.get_x() < 0:
            continue
        elif hero.get_y() < 0:
            hero.move_left()
        elif hero.get_x() < 0:
            hero.move_up()
        else:
            hero.move_up_left()
    elif pressed[pygame.K_w] and pressed[pygame.K_d]:
        if hero.get_y() < 0 and hero.get_x() + hero.width > screen_width:
            continue 
        elif hero.get_y() < 0:
            hero.move_right()
        elif hero.get_x() + hero.width > screen_width:
            hero.move_up()
        else:
            hero.move_up_right()
    elif pressed[pygame.K_s] and pressed[pygame.K_a]:
        if hero.get_x() < 0 and  hero.get_y() + hero.height > screen_height:
            continue
        elif hero.get_y() + hero.height > screen_height:
            hero.move_left()
        elif hero.get_x() < 0:
            hero.move_down()
        else:
            hero.move_down_left()
    elif pressed[pygame.K_s] and pressed[pygame.K_d]:
        if hero.get_x() + hero.width > screen_width and  hero.get_y() + hero.height > screen_height:
            continue
        elif hero.get_y() + hero.height > screen_height:
            hero.move_right()
        elif hero.get_x() + hero.width > screen_width:
            hero.move_down()
        else:
            hero.move_down_right()
    elif pressed[pygame.K_w] and hero.get_y() > 0:
        hero.move_up()
    elif pressed[pygame.K_s] and hero.get_y() + hero.height < screen_height:
        hero.move_down()
    elif pressed[pygame.K_a] and hero.get_x() > 0:
        hero.move_left()
    elif pressed[pygame.K_d] and hero.get_x() + hero.width < screen_width:
        hero.move_right()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), hero.get_rectangle())
    for bullet in hero.all_bullets:
        bullet.move_in_direction()
        pygame.draw.rect(screen, (0, 128, 255), bullet.get_rectangle())
    pygame.display.flip()
