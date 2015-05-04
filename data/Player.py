from Mallet import Mallet


class TooManyPointsException(Exception):
    """Raised when player has more points than he can according to rules."""
    pass


class Player:
    """Represents player with his name, points and mallet."""

    # TODO: Decide value of max points in sth like game rules, probably implemented in another class
    MAX_POINTS = 10     # temp

    def __init__(self, player_id, points):
        self._player_id = player_id
        self._points = points
        #self._mallet = mallet #mallet yet has a player assigned to it.
        self._name = ''

    @property
    def name(self):
        return self._name

    @property
    def player_id(self):
        return self._player_id

    @property
    def points(self):
        return self._points

#    @property
#    def mallet(self):
#        return self._mallet

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



