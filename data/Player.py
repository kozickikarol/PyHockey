from __future__ import division
from Mallet import Mallet


class TooManyPointsException(Exception):
    """Raised when player has more points than he can according to rules."""
    pass


class Player:
    """
    Class for representing player
    """

    PLAYER_RED = 1
    PLAYER_BLUE = 2

    # TODO: Decide value of max points in sth like game rules, probably implemented in another class
    MAX_POINTS = 10     # temp

    def __init__(self, player_id, pitch):
        """
        initializes Player object and creates underlying Mallet

        :param playerColor: defines which player are you creating (MalletInterface.PLAYER_RED || BLUE)
        """
        if player_id == self.PLAYER_RED:
            self.playerColor = self.PLAYER_RED
            self._borders = ((pitch.i_min, (pitch.i_min+pitch.i_max)/2), (pitch.j_min, pitch.j_max))
            self._center = (200, 300)
        else:
            self.playerColor = self.PLAYER_BLUE
            self._borders = (((pitch.i_min+pitch.i_max)/2, pitch.i_max), (pitch.j_min, pitch.j_max))
            self._center = (600, 300)

        self._points = 0
        self._name = ''
        self._player_id = player_id

        self._mallet = Mallet(26, self._center[0], self._center[1], 100, self, pitch, self._borders)

    @property
    def name(self):
        return self._name

    @property
    def player_id(self):
        return self._player_id

    @property
    def points(self):
        return self._points

    @property
    def mallet(self):
       return self._mallet

    @name.setter
    def name(self, name):
        self._name = name

    def clearPoints(self):
        """When new round or set begins, player should have 0 points"""
        self._points = 0

    def addPoint(self):
        """Should be called when player scores a goal."""
        self._points += 1
        if self._points >= self.MAX_POINTS:
            raise TooManyPointsException


    def printTooManyPointsInfo(self):
        print("Player " + self.name + " has won scoring " + str(self.MAX_POINTS) + " points.")
