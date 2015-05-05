from __future__ import division
import os
from sys import exit
import pygame as pg
from pygame.locals import *
from data.Disc import Disc
from data.Pitch import Pitch

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

        self.pitch = Pitch()
        self.discs = [Disc(50, 50, 10, 1), Disc(30, 30, 10, 1), Disc(15, 15, 10, 1)]
        self.mallets = []

        self.loop()

    def loop(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.discs[0].vel.x -= 1
                    elif event.key == K_RIGHT:
                        self.discs[0].vel.x += 1
                    elif event.key == K_DOWN:
                        self.discs[0].vel.y += 1
                    elif event.key == K_UP:
                        self.discs[0].vel.y -= 1

            for disc in self.discs:
                disc.friction()
                axis = self.pitch.is_border_collision(disc)
                if axis:
                    disc.border_collision(axis)

            # Detect and react on collisions between discs
            for i in range(len(self.discs)-1):
                for j in range(i, len(self.discs)):
                    self.discs[i].circle_collision(self.discs[j])

            for disc in self.discs+self.mallets:
                disc.pos.x += disc.vel.x
                disc.pos.y += disc.vel.y

            #TODO: Drawing tool
            for disc in self.discs+self.mallets:
                pg.draw.circle(self.screen, (255, 255, 255), (int(disc.pos.x), int(disc.pos.y)), disc.radius)

            pg.display.update()
        exit()