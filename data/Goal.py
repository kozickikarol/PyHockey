__author__ = 'Asia'


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
            raise WrongTypeException
        self.j_min = 30
        self.j_max = 45
        self.i = v

    def in_goal(self, i, j, r):
        """
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: true if the disk has fallen into, false - if it haven't
        :raise: WrongTypeException if i, j or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        if not type(i) == int or not type(j) == int or not type(r) == int:
            raise WrongTypeException
        if i + r > self.i_max or i - r < self.i_min or j + r > self.j_max or j - r < self.j_min:
            raise OutOfRangeException
        if self.i == i + r and j + r > self.j_min and j + r < self.j_max:
            return True
        else:
            return False

