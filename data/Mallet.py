import pygame
from data.DrawableInterface import Drawable
from data.MalletInterface import MalletInterface
from data.Kinematics import PhysicsObject


class Mallet(MalletInterface, PhysicsObject, Drawable):

    def __init__(self, radius, pos_x, pos_y, mass, player, pitch, borders):
        # TODO WRITE DOC STRINGS!!!
        """

        :param radius: Size of mallet (units?)
        :param color: defines which player are you creating (MalletInterface.PLAYER_RED || BLUE)
        :param position: position of player (class Point)
        """

        MalletInterface.__init__(self)
        PhysicsObject.__init__(self, pos_x, pos_y, mass, radius, borders)
        #super(Mallet, self).__init__()
        self._color = player.playerColor
        self._pitch = pitch
        self._picture_path = "resources/graphics/redmallet.png"
        self._player = player

        self._image = pygame.transform.scale(pygame.image.load(self._picture_path), (2*radius, 2*radius))

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
    def pitch(self):
        return self._pitch

    @property
    def pos(self):
        return self._pos

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, v):
        self._vel = v

    @direction.setter
    def direction(self, d):
        self.vel.angle = d


    #def move_by(self, x, y):
    #    self._pos.change_state((x, y))
    #    self.fix_position()

    def move_to(self, x, y):
        from data.Kinematics import Vector
        move_vector = Vector(x, y) - self._pos
        if move_vector.length > PhysicsObject.MAX_MALLET_VELOCITY:
            move_vector.length = PhysicsObject.MAX_MALLET_VELOCITY
        self.pos.state = (self._pos.x + move_vector.x, self._pos.y + move_vector.y)
        self.correct_position_in_borders()

    def load_image(self):
        from Player import Player
        if self._player.playerColor == Player.PLAYER_BLUE:
            self._image = pygame.image.load("resources/graphics/bluemallet.png")
        elif self._player.playerColor == Player.PLAYER_RED:
            self._image = pygame.image.load("resources/graphics/redmallet.png")
        else:
            raise ValueError('Invalid value for player (' + self._player.playerColor + ')')

    """def fix_position(self):
        x_min, x_max = self._borders[0]
        y_min, y_max = self._borders[1]
        if self.pos.x - self.radius < x_min:
            self.pos.x = x_min+self.radius
        if self.pos.x + self.radius > x_max:
            self.pos.x = x_max-self.radius
        if self.pos.y - self.radius < y_min:
            self.pos.y = y_min+self.radius
        if self.pos.y + self.radius > y_max:
            self.pos.y = y_max-self.radius"""

    def print_properties(self):
        print self.velocity
        print self.direction
        print self.pos
        print self.color
        print self.radius
