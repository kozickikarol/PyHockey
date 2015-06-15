__author__ = 'Asia'
from Logger import Logger

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


class Goal:
    """
    class represent a goal on the Pitch
    """
    def __init__(self, v):
        """
        define constructor of class Goal. If the value will not be equal 'L' or 'R', the function raise the ValueError
        :param v: x layout of the goal
        :return: none
        :raise: WrongTypeException if v is not type of int
        """
        if not type(v) == int:
            Logger.error("GOAL: init Wrong type!")
            raise WrongTypeException
        self.j_min = 30
        self.j_max = 45
        self.i = v
        Logger.debug("GOAL: init(jmin=%s, jmax=%s, v=%s)", str(self.j_min), str(self.j_max), str(v))

    def in_goal(self, i, j, r):
        """
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: true if the disk has fallen into, false - if it haven't
        :raise: WrongTypeException if i, j or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        Logger.debug("GOAL: in_goal(i=%s, j=%s, r=%s)", str(i), str(j), str(r))
        if not type(i) == int or not type(j) == int or not type(r) == int:
            Logger.error("GOAL: in_goal - Wrong type!")
            raise WrongTypeException
        if i + r > self.i_max or i - r < self.i_min or j + r > self.j_max or j - r < self.j_min:
            Logger.error("GOAL: in_goal - Out of range!")
            raise OutOfRangeException
        if self.i == i + r and j + r > self.j_min and j + r < self.j_max:
            Logger.debug("GOAL: in_goal returned True")
            return True
        else:
            Logger.debug("GOAL: in_goal returned False")
            return False

