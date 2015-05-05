import os
from sys import exit
import pygame as pg
from pygame.locals import *


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


        self.loop()

    def loop(self):
        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True
        exit()