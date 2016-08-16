import unit
import pygame


class Hero(unit.Unit):
    all_bullets = []

    def shoot_up(self):
        self.all_bullets.append(pygame.Rect(self.get_x(), self.get_y(), 30, 30))
