import pygame
import math


class Unit:
    base_speed = 500
    move_speed = 0

    def __init__(self, x, y, width, height, base_speed):
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(x, y, width, height)
        self.base_speed = base_speed

    def diagonal_movement(self):
        diagonal_move_speed = math.sqrt((self.move_speed ** 2) / 2)
        return diagonal_move_speed

    def move_left(self):
        self.rectangle = self.rectangle.move(-self.move_speed, 0)

    def move_right(self):
        self.rectangle = self.rectangle.move(self.move_speed, 0)

    def move_down(self):
        self.rectangle = self.rectangle.move(0, self.move_speed)

    def move_up(self):
        self.rectangle = self.rectangle.move(0, -self.move_speed)

    def move_up_left(self):
        diagonal_move_speed = self.diagonal_movement()
        self.rectangle = self.rectangle.move(-diagonal_move_speed, -diagonal_move_speed)

    def move_up_right(self):
        diagonal_move_speed = self.diagonal_movement()
        self.rectangle = self.rectangle.move(diagonal_move_speed, -diagonal_move_speed)

    def move_down_left(self):
        diagonal_move_speed = self.diagonal_movement()
        self.rectangle = self.rectangle.move(-diagonal_move_speed, diagonal_move_speed)

    def move_down_right(self):
        diagonal_move_speed = self.diagonal_movement()
        self.rectangle = self.rectangle.move(diagonal_move_speed, diagonal_move_speed)

    def get_rectangle(self):
        return self.rectangle

    def get_x(self):
        return self.rectangle.x

    def get_y(self):
        return self.rectangle.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
