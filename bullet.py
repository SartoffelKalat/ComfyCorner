import unit


class Bullet(unit.Unit):
    direction_up = "UP"
    direction_down = "DOWN"
    direction_left = "LEFT"
    direction_right = "RIGHT"

    def __init__(self, x, y, width, height, direction):
        super(Bullet, self).__init__(x, y, width, height, 1000)
        self.direction = direction

    def get_direction(self):
        return self.direction

    def move_in_direction(self):
        if self.direction in self.direction_up:
            self.move_up()
        elif self.direction in self.direction_down:
            self.move_down()
        elif self.direction in self.direction_left:
            self.move_left()
        elif self.direction in self.direction_right:
            self.move_right()
