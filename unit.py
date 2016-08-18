import pygame
import math


class Unit:
    def diagonal_movement(self, move_speed):
        move_speed = math.sqrt((move_speed ** 2) / 2)
        return move_speed

    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(x, y, width, height)

    def move_left(self, move_speed):
        self.rectangle = self.rectangle.move(-move_speed, 0)

    def move_right(self, move_speed):
        self.rectangle = self.rectangle.move(move_speed, 0)

    def move_down(self, move_speed):
        self.rectangle = self.rectangle.move(0, move_speed)

    def move_up(self, move_speed):
        self.rectangle = self.rectangle.move(0, -move_speed)

    def move_up_left(self, move_speed):
        move_speed = self.diagonal_movement(move_speed)
        self.rectangle = self.rectangle.move(-move_speed, -move_speed)

    def move_up_right(self, move_speed):
        move_speed = self.diagonal_movement(move_speed)
        self.rectangle = self.rectangle.move(move_speed, -move_speed)

    def move_down_left(self, move_speed):
        move_speed = self.diagonal_movement(move_speed)
        self.rectangle = self.rectangle.move(-move_speed, move_speed)

    def move_down_right(self, move_speed):
        move_speed = self.diagonal_movement(move_speed)
        self.rectangle = self.rectangle.move(move_speed, move_speed)

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
