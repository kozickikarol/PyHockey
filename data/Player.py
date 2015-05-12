from __future__ import division
from data.Mallet import Mallet


class Player(object):
    """
    Class for representing player
    """
    PLAYER_RED = 1
    PLAYER_BLUE = 2

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

        self.mallet = Mallet(26, self._center[0], self._center[1], 100, self, pitch, self._borders)
