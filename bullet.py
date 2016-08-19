import unit


class Bullet(unit.Unit):
    direction_up = "UP"
    direction_down = "DOWN"
    direction_left = "LEFT"
    direction_right = "RIGHT"
    move_speed_bullet = 10

    def __init__(self, x, y, width, height, direction):
        super(Bullet, self).__init__(x, y, width, height)
        self.direction = direction

    def get_direction(self):
        return self.direction

    def move_in_direction(self):
        if self.direction in self.direction_up:
            self.move_up(self.move_speed_bullet)
        elif self.direction in self.direction_down:
            self.move_down(self.move_speed_bullet)
        elif self.direction in self.direction_left:
            self.move_left(self.move_speed_bullet)
        elif self.direction in self.direction_right:
            self.move_right(self.move_speed_bullet)
