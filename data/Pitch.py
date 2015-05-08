import pygame
from data.DrawableInterface import Drawable
from data.Kinematics import Point

__author__ = 'Asia'

from Goal import Goal


class WrongTypeException(Exception):
    """
    raised when the parameter is wrong type
    """
    pass


class OutOfRangeException(Exception):
    """
    raised when the disk is out of the pitch
    """
    pass


class Pitch(Drawable):
    """
    class represent a pitch on which the game will take a place
    """

    def __init__(self):
        """
        define constructor of class Pitch.
        """
        self.i_min = 0
        self.i_max = 100
        self.j_min = 0
        self.j_max = 75
        self.i_border = 50
        self.left_goal = Goal(0)
        self.right_goal = Goal(100)

        #drawable part
        # TODO better pitch image
        self.image = pygame.image.load("resources/graphics/pitch.png")
        self.position = Point(0, 0)

    def collision(self, i, j, r):
        """
        check a collision between disk and a border of the pitch
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: true if the collision between a disk and the border of pitch have taken place, false - if it haven't
        :raise: WrongTypeException if i, j or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        if not type(i) == int or not type(j) == int or not type(r) == int:
            raise WrongTypeException
        if i + r > self.i_max or i - r < self.i_min or j + r > self.j_max or j - r < self.j_min:
            raise OutOfRangeException
        if self.i_min == i - r or self.i_max == i + r or self.j_min == j - r or self.j_max == j + r:
            return True
        else:
            return False

    def left_half(self, ii, r):
        """
        check in which half of the pitch the disk is situated
        :param ii: x coordinates of disk
        :return: true if the disk is on left player half of pitch, false if it is not
        :raise: WrongTypeException if ii or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        if not type(ii) == int or not type(r) == int:
            raise WrongTypeException
        if ii + r > self.i_max or ii - r < self.i_min:
            raise OutOfRangeException
        if ii < self.i_border:
            return True
        else:
            return False

    def right_half(self, ii, r):
        """
        check in which half of the pitch the disk is situated
        :param ii: x coordinates of disk
        :return: true if the disk is on right player half of pitch, false if it is not
        :raise: WrongTypeException if ii or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        if not type(ii) == int or not type(r) == int:
            raise WrongTypeException
        if ii + r > self.i_max or ii - r < self.i_min:
            raise OutOfRangeException
        if ii > self.i_border:
            return True
        else:
            return False