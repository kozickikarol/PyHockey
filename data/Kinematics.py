import math


class Point:
    """Point in 2D"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def toArray(self):
        return [self.x, self.y]

class Velocity:
    def __init__(self, v_x, v_y):
        self.v_x = v_x
        self.v_y = v_y

    def value(self):
        return math.sqrt(self.v_x ** 2 + self.v_y ** 2)

    def change(self, diff_x, diff_y):
        self.v_x += diff_x
        self.v_y += diff_y

    def setCoords(self, v_x, v_y):
        self.v_x = v_x
        self.v_y = v_y

