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
    #def __init__(self, v): #what is v?
    def __init__(self, x, y_center, width, goal_type):
        """
        define constructor of class Goal. If the value will not be equal 'L' or 'R', the function raise the ValueError
        :param x: x position
        :param y_center: y coordinate of the center of goal
        :param width: width of goal which is measured along y axis.
        :param goal_type: 'l' for left and 'r' for right goal
        :return: none
        :raise: WrongTypeException if v is not type of int
        """
        #:param v: x layout of the goal #??
        self.j_min = y_center - 0.5 * width
        self.j_max = y_center + 0.5 * width
        self.i = x
        self.goal_type = goal_type

    def in_goal(self, i, j, r):
        """
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :return: True if goal scored, false otherwise
        :raise: WrongTypeException if i, j or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        # another (currently unused) solution: :return: -1 if left goal scored, 1 if right goal, 0 if goal hasn't been scored.
        if not type(i) == int or not type(j) == int or not type(r) == int:
            raise WrongTypeException
        # see: Pitch::is_border_collision()
        #if i + r > self.i_max or i - r < self.i_min or j + r > self.j_max or j - r < self.j_min:
        #    raise OutOfRangeException
        if self.goal_type == 'l':
            if i - self.i < r and self.j_min + r < j < self.j_max - r:
                return True
        #        return -1
            else:
                return False
                #return 0
        elif self.goal_type == 'r':
            if self.i - i < r and self.j_min + r < j < self.j_max - r:
                return True
                #return 1
            else:
                return False
                #return 0

