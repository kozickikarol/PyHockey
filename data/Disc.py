import pygame

from data.DrawableInterface import Drawable
from data.Kinematics import *


class Disc(Drawable):
    def __init__(self):
        self.__position = Point(0, 0)
        # TODO: radius length depends on the Pitch size
        self.__radius = 50
        self.__velocity = Velocity(0, 0)
        self.__picture_path = "resources/graphics/disc.png"

        self.image = pygame.transform.scale(pygame.image.load(self.__picture_path), (self.radius, self.radius))

    # TODO: Use some drawing to display the picture on a pitch
    # Use position, radius, picture_path


    @property
    def position(self):
        return self.__position

    @property
    def velocity(self):
        return self.__velocity

    @property
    def radius(self):
        return self.__radius

    @property
    def picture_path(self):
        return self.__picture_path

    def moveTo(self, x, y):
        self.position.moveTo(x, y)

    def move(self, x_move, y_move):
        self.position.move(x_move, y_move)

    def accelerate(self, v_x_diff, v_y_diff):
        self.velocity.change(v_x_diff, v_y_diff)

    @velocity.setter
    def velocity(self, v_x, v_y):
        self.velocity.setCoords(v_x, v_y)

    def printStatus(self):
        print("Position: " + self.position.x + ", " + self.position.y)
        print("Velocity: " + self.velocity.v_x + ", " + self.velocity.v_y)
        print("Velocity value: " + self.velocity.value())