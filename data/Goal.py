__author__ = 'Asia'

import math


class Goal:
    """
    class represent a goal on the Pitch
    """
    def __init__(self, v):
        """
        define constructor of class Goal. If the value will not be equal 'L' or 'R', the function raise the ValueError
        :param v: x layout of the goal
        :return: none
        """
        self.i_min = 30
        self.j_max = 45
        self.i = v

    def in_goal(self, i, j, r):
        """
        method return true if the disk has fallen into, false - if it haven't
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: none
        """
        if math.fabs(self.i - r) == i and j > math.fabs(self.j_min - r):
            return True
        else:
            return False