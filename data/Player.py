from data.Kinematics import Point
from data.Mallet import Mallet


class Player(object):
    """
    Class for representing player
    """

    def __init__(self, playerColor):
        """
        initializes Player object and creates underlying Mallet

        :param playerColor: defines which player are you creating (MalletInterface.PLAYER_RED || BLUE)
        """
        self.playerColor = playerColor

        # TODO consider calculating radius and position based on pitch size and players color
        self.mallet = Mallet(20, playerColor, Point((playerColor * 100) + 50, 50))