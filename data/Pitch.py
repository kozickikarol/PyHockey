__author__ = 'Asia'

from Goal import Goal


class Pitch:
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

    def collision(self, i, j, r):
        """
        check a collision between disk and a border of the pitch
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: true if the collision between a disk and the border of pitch have taken place, false - if it haven't
        """
        if self.i_min + r == i or self.i_max - r == i or self.j_min + r == j or self.j_max - r == j:
            return True
        else:
            return False

    def left_half(self, i):
        """
        check in which half of the pitch the disk is situated
        :param i: x coordinates of disk
        :return: true if the disk is on left player half of pitch, false if it is not
        """
        if i < self.i_border:
            return True
        else:
            return False

    def right_half(self, i):
        """
        check in which half of the pitch the disk is situated
        :param i: x coordinates of disk
        :return: true if the disk is on right player half of pitch, false if it is not
        """
        if i < self.i_border:
            return True
        else:
            return False