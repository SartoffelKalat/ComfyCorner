import pygame


class Unit:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height;
        self.rectangle = pygame.Rect(x, y, width, height)

    def move_left(self, move_speed):
        self.rectangle = self.rectangle.move(-move_speed, 0)

    def move_right(self, move_speed):
        self.rectangle = self.rectangle.move(move_speed, 0)

    def move_down(self, move_speed):
        self.rectangle = self.rectangle.move(0, move_speed)

    def move_up(self, move_speed):
        self.rectangle = self.rectangle.move(0, -move_speed)

    def get_rectangle(self):
        return self.rectangle
