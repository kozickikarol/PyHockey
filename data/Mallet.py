from data.MalletInterface import MalletInterface
from data.Kinematics import PhysicsObject

class Mallet(MalletInterface, PhysicsObject):

    def __init__(self, player, radius, pos_x, pos_y, mass, pitch):
        MalletInterface.__init__(self, player)
        PhysicsObject.__init__(self, pos_x, pos_y, radius, mass)
        self.load_image()
        self._pitch = pitch

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
    def pitch(self):
        return self._pitch

    @property
    def position_x(self):
        return self._pos.state[0]

    @property
    def position_y(self):
        return self._pos.state[1]

    @property
    def velocity(self):
        return self._vel

    @velocity.setter
    def velocity(self, v):
        self._vel = v

    @direction.setter
    def direction(self, d):
        self._vel.angle = d

    def draw(self):
        # TODO: no class for the display available atm
        # something like display.draw(self.__image, x , y) ?
        pass

    def move_by(self, x, y):
        self._vel.change_state((x, y))
        self.fix_position()

    def move_to(self, x, y):
        self._vel.state = (x, y)
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
        if self.player == MalletInterface.PLAYER_BLUE:
            if self.pitch.right_half(self.position_x, self.radius):
                self.move_to(self.pitch.i_border-self.radius, self.position_y)
        elif self.player == MalletInterface.PLAYER_RED:
            if self.pitch.left_half(self.position_x, self.radius):
                self.move_to(self.pitch.i_border+self.radius, self.position_y)
        else:
            raise ValueError('Invalid value for player(' + self._player + ')')
