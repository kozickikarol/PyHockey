from __future__ import division
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
        self.pitch = Pitch()
        self.players = [Player(Player.PLAYER_RED, self.pitch), Player(Player.PLAYER_BLUE, self.pitch)]
        self.mallets = [self.players[0].mallet, self.players[1].mallet]
        pitch_borders = [(self.pitch.i_min, self.pitch.i_max), (self.pitch.j_min, self.pitch.j_max)]
        self.discs = [Disc(100, 100, 1, 26, pitch_borders), Disc(30, 30, 1, 26, pitch_borders)]
        self.objects = self.discs+self.mallets

        # everything that will be drawn
        self.drawables = [self.pitch]
        self.drawables.extend(self.mallets)
        self.drawables.extend(self.discs)

        self.loop()

    def loop(self):
        black = (0, 0, 0)

        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True
                #only for test purposes
                elif event.type == pg.MOUSEMOTION:
                    self.players[0].mallet.vel.state = event.rel
                    self.players[0].mallet.move_to(*event.pos)

            # dummy line to check if it actually works
            # self.players[0].mallet.position.move(5, 0)

            # reset screen
            self.screen.fill(black)

            for object in self.objects:
                object.friction()
                axis = self.pitch.is_border_collision(object)
                if axis:
                    object.border_collision(axis)

            # Detect and react on collisions between discs
            for i in range(len(self.objects)-1):
                for j in range(i, len(self.objects)):
                    self.objects[i].circle_collision(self.objects[j])

            for disc in self.discs:
                disc.move(disc.vel.x, disc.vel.y)

            # draw everything
            for drawable in self.drawables:
                drawable.draw(self.screen)

            # update display
            pg.display.flip()

        exit()