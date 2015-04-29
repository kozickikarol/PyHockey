from data.MalletInterface import MalletInterface


class Mallet(MalletInterface):


    def __init__(self, player, radius, pos_x, pos_y):
        super(Mallet, self).__init__(player)
        self._radius = radius
        self._pos_x = pos_x
        self._pos_y = pos_y
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
    def player(self):
        return self._player

    @property
    def position_x(self):
        return self._pos_x

    @property
    def velocity(self):
        return self._velocity

    @property
    def position_y(self):
        return self._pos_y

    @velocity.setter
    def velocity(self, v):
        self._velocity = v

    @direction.setter
    def direction(self, d):
        self._direction = d

    def draw(self):
        # TODO: no class for the display available atm
        # something like display.draw(self.__image, x , y) ?
        pass

    def move_by(self, x, y):
        self._pos_x += x
        self._pos_y += y
        # TODO: reconsider and discuss checking and correction mechanism
        self.fix_position()

    def move_to(self, x, y):
        self._pos_x = x
        self._pos_y = y
        self.fix_position()

    def load_image(self):
        if self._player == MalletInterface.PLAYER_BLUE:
            # TODO: load picture from resources/graphics/bluemallet.png
            pass
        elif self._player == MalletInterface.PLAYER_RED:
            # TODO: load picture from resources/graphics/redmallet.png
            pass
        else:
            raise ValueError('Invalid value for player (' + self._player + ')')

    def fix_position(self):
        # TODO: no way to get player area's boundaries,
        # if pos_x < min_x
        #   pos_x = min_x
        # etc...
        pass

    def print_properties(self):
        print self.velocity
        print self.direction
        print self.position_x
        print self.position_y
        print self.player
        print self.radius
