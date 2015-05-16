from __future__ import division
from Player import Player
import time


class GameTime:
    # TODO: Decide value of max time in sth like game rules, probably implemented in another class
    MAX_TIME = 1     # [minutes]

    startTime = time.clock()

    def __init__(self):
        pass

    @staticmethod
    def startMeasuring():
        """This method should be called at start of game so that it starts measuring time"""
        GameTime.startTime = time.time()

    @staticmethod
    def getCurrentGameTime():
        game_time = time.time() - GameTime.startTime
        minutes = int(game_time) // 60
        seconds = int(game_time) % 60
        if minutes >= GameTime.MAX_TIME:
            raise OutOfGameTimeException
        return minutes, seconds


class OutOfGameTimeException(Exception):
    """Raised when time of game is over."""
    pass


class ScoreBoard:
    """Represents the board on which scores and time are displayed."""
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    # TODO: graphic version
    def displayScore(self):
        """Text version displaying points scored by players"""
        print(self._player1.name + " " + str(self._player1.points) + ":" +
              str(self._player2.points) + " " + self._player2.name)

    # TODO: graphic version
    def displayTime(self):
        """Text version displaying game time"""
        h, m = GameTime.getCurrentGameTime()
        print("Time: " + str(h) + ":" + str(m))

    def displayTimeExceptionally(self):
        print("Time: " + str(GameTime.MAX_TIME) + ":00")
        print("Game time is over!")

    def display(self):
        try:
            self.displayTime()
        except OutOfGameTimeException:
            self.displayTimeExceptionally()
        self.displayScore()
        print("\n")



