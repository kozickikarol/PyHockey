from abc import ABCMeta, abstractmethod, abstractproperty
from data.DrawableInterface import Drawable


class MalletInterface(Drawable):

    def __init__(self):
        self._color = None
        self._pitch = None

    @abstractproperty
    def color(self):
        pass

    @abstractproperty
    def position(self):
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
    def load_image(self):
        pass




