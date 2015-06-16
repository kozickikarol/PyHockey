import pygame
from data.DrawableInterface import Drawable
from data.MalletInterface import MalletInterface
from data.Kinematics import PhysicsObject
from Logger import Logger

class Mallet(MalletInterface, PhysicsObject, Drawable):

    def __init__(self, radius, pos_x, pos_y, mass, player, borders):
        """
        Initialize Mallet object
        :param radius: int/float radius of Mallet
        :param pos_x: int/float - x position of Mallet
        :param pos_y: int/float - x position of Mallet
        :param mass: mass of Mallet
        :param player: Player - Mallet owner
        :param borders: list of tuples - borders in which mallet can move
        :return:
        """

        MalletInterface.__init__(self)
        PhysicsObject.__init__(self, pos_x, pos_y, mass, radius, borders)
        self._player = player
        self.load_image()


    @property
    def image(self):
        Logger.debug("MALLET: image accessed")
        return self._image

    @property
    def direction(self):
        Logger.debug("MALLET: direction accessed, returned %s", str(self._direction))
        return self._direction

    @property
    def radius(self):
        Logger.debug("MALLET: radius accessed, returned %s", str(self._radius))
        return self._radius

    @property
    def pos(self):
        Logger.debug("MALLET: pos accessed, returned %s", str(self._pos))
        return self._pos

    @property
    def vel(self):
        Logger.debug("MALLET: vel accessed, returned %s", str(self._vel))
        return self._vel

    @vel.setter
    def vel(self, v):
        Logger.debug("MALLET: vel.setter(%s)", str(v))
        self._vel = v

    @direction.setter
    def direction(self, d):
        Logger.debug("MALLET: direction.setter(%s)", str(d))
        self.vel.angle = d


    #def move_by(self, x, y):
    #    self._pos.change_state((x, y))
    #    self.fix_position()

    def move_to(self, x, y):
        from data.Kinematics import Vector
        Logger.debug("MALLET: move_to(%s,%s) pos before =%s", str(x), str(y), str(self._pos))
        move_vector = Vector(x, y) - self._pos
        if move_vector.length > PhysicsObject.MAX_MALLET_VELOCITY:
            move_vector.length = PhysicsObject.MAX_MALLET_VELOCITY
        self.pos.state = (self._pos.x + move_vector.x, self._pos.y + move_vector.y)
        Logger.debug("MALLET: move_to(%s,%s) pos after =%s", str(x), str(y), str(self._pos))

        self.correct_position_in_borders()
        Logger.debug("MALLET: move_to(%s,%s) pos after position correction=%s", str(x), str(y), str(self._pos))

    def load_image(self):
        """
        Method used to load sprite for Mallet according to Player.
        :return: None
        """
        from Player import Player
        if self._player.playerColor == Player.PLAYER_BLUE:
            Logger.debug("MALLET: load_image playerColor = PLAYER_BLUE")
            image = "resources/graphics/bluemallet.png"
        elif self._player.playerColor == Player.PLAYER_RED:
            Logger.debug("MALLET: load_image playerColor = PLAYER_RED")
            image = "resources/graphics/redmallet.png"
        else:
            Logger.error("MALLET: Invalid value for player (" + self._player.playerColor + ")")
            raise ValueError('Invalid value for player (' + self._player.playerColor + ')')
        self._image = pygame.transform.scale(pygame.image.load(image), (int(2*self.radius), int(2*self.radius)))

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
        print self.radius
