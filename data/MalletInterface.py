from abc import ABCMeta, abstractmethod, abstractproperty



class MalletInterface:
    __metaclass__ = ABCMeta

    PLAYER_RED = 1
    PLAYER_BLUE = 2

    def __init__(self, player):
        self._player = player
        self._velocity = None
        self._radius = None
        self._direction = None
        self._image = None
        self._pos_x = None
        self._pos_y = None
        self._pitch = None

    @abstractproperty
    def player(self):
        pass

    @abstractproperty
    def position_x(self):
        pass

    @abstractproperty
    def position_y(self):
        pass

    @abstractproperty
    def image(self):
        pass

    @abstractproperty
    def radius(self):
        pass

    @abstractproperty
    def velocity(self):
        pass

    @abstractproperty
    def direction(self):
        pass

    @abstractproperty
    def pitch(self):
        pass

    @abstractmethod
    def move_to(self, x, y):
        pass

    @abstractmethod
    def move_by(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def load_image(self):
        pass




