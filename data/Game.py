import os
from sys import exit
import pygame as pg
from pygame.locals import *
from data.Disc import Disc
from data.MalletInterface import MalletInterface
from data.Pitch import Pitch
from data.Player import Player


class Game(object):
    def __init__(self, size):
        pg.init()
        pg.display.set_caption("PyHockey")
        self.screensize = (int(size[0]), int(size[1]))

        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.screen = pg.display.set_mode(self.screensize)

        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False

        # model part
        self.players = [Player(MalletInterface.PLAYER_BLUE), Player(MalletInterface.PLAYER_RED)]
        self.disc = Disc()
        self.pitch = Pitch()

        # everything that will be drawn
        self.drawables = [self.pitch, self.players[0].mallet, self.players[1].mallet, self.disc]

        self.loop()

    def loop(self):
        black = (0, 0, 0)

        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True

            # dummy line to check if it actually works
            # self.players[0].mallet.position.move(5, 0)

            # reset screen
            self.screen.fill(black)

            # draw everything
            for drawable in self.drawables:
                drawable.draw(self.screen)

            # update display
            pg.display.flip()

        exit()