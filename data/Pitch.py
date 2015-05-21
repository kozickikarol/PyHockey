import pygame
from data.DrawableInterface import Drawable
from data.Kinematics import Point

__author__ = 'Asia'

from Goal import Goal
from Disc import Disc
from Mallet import Mallet
from Kinematics import Vector

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
        #TODO: goal width should be dependent on graphics.
        goal_width = 30

        self.i_min = 0
        self.i_max = 800
        self.j_min = 0
        self.j_max = 600
        self.i_border = 50
        j_middle = 0.5 * (self.j_min + self.j_max)
        self.left_goal = Goal(self.i_min, j_middle, goal_width, 'l')
        self.right_goal = Goal(self.i_max, j_middle, goal_width, 'r')

        #drawable part
        # TODO better pitch image
        self._image = pygame.image.load("resources/graphics/pitch.png")
        self._pos = Vector(0, 0)


    #TODO: add unittests
    #TODO: There is some issue, sometimes disc sticks on border - rewrite collision checking
    def is_border_collision(self, object):
        """
        check a collision between disk and a border of the pitch
        :param object: object with x,y,radius parameters
        :return: 'x' or 'y' if the collision between a disk/mallet and the border of pitch have taken place, false - if it haven't
        :raise: WrongTypeException if object is not type of disc/mallet
        """
        #TODO: Is there a way to do it better ?
        if not isinstance(object, Disc) and not isinstance(object, Mallet):
            raise WrongTypeException
        if object.pos.x - object.radius < self.i_min or object.pos.x + object.radius > self.i_max:
            return 'x'
        if object.pos.y - object.radius < self.j_min or object.pos.y + object.radius > self.j_max:
            return 'y'
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