import pygame
from data.DrawableInterface import Drawable
from data.MalletInterface import MalletInterface


class Mallet(MalletInterface, Drawable):

    def __init__(self, radius, color, position):
        # TODO WRITE DOC STRINGS!!!
        """

        :param radius: Size of mallet (units?)
        :param color: defines which player are you creating (MalletInterface.PLAYER_RED || BLUE)
        :param position: position of player (class Point)
        """
        #super(Mallet, self).__init__()
        self._radius = radius
        self._color = color
        self.position = position
        self._velocity = 0
        self._direction = 0
        self.load_image()

    @property
    def image(self):
        return self._image

    @property
    def direction(self):
        return self._direction

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    @property
    def velocity(self):
        return self._velocity

    @property
    def position(self):
        return self.position

    @velocity.setter
    def velocity(self, v):
        self._velocity = v

    @direction.setter
    def direction(self, d):
        self._direction = d


    def move_by(self, x, y):
        self._pos_x += x
        self._pos_y += y
        # TODO: reconsider and discuss checking and correction mechanism
        self.fix_position()

    def move_to(self, x, y):
        self.position.x = x
        self.position.y = y
        self.fix_position()

    def load_image(self):
        if self._color == MalletInterface.PLAYER_BLUE:
            self.image = pygame.image.load("resources/graphics/bluemallet.png")
        elif self._color == MalletInterface.PLAYER_RED:
            self.image = pygame.image.load("resources/graphics/redmallet.png")
        else:
            raise ValueError('Invalid value for player (' + self._color + ')')

    def fix_position(self):
        # TODO: no way to get player area's boundaries,
        # if pos_x < min_x
        # pos_x = min_x
        # etc...
        pass

    def print_properties(self):
        print self.velocity
        print self.direction
        print self.position_x
        print self.position_y
        print self.player
        print self.radius