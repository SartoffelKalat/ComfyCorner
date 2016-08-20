import unit
from bullet import Bullet


class Hero(unit.Unit):
    all_bullets = []

    def __init__(self, x, y, width, height):
        super(Hero, self).__init__(x, y, width, height, 500)

    def __middle_x_hero(self, bullet_width):
        return self.get_x() + (self.get_width() / 2) - (bullet_width / 2)

    def __middle_y_hero(self, bullet_height):
        return self.get_y() - (bullet_height / 2) + (self.get_height() / 2)

    def __shoot(self, direction):
        self.all_bullets.append(
            Bullet(self.__middle_x_hero(30), self.__middle_y_hero(30), 30, 30, direction))

    def shoot_up(self):
        self.__shoot(Bullet.direction_up)

    def shoot_down(self):
        self.__shoot(Bullet.direction_down)

    def shoot_left(self):
        self.__shoot(Bullet.direction_left)

    def shoot_right(self):
        self.__shoot(Bullet.direction_right)
