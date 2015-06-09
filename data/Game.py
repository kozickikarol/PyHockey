from __future__ import division
import os
import pygame as pg
import cv2
import numpy as np
from pygame.locals import *
from data.Disc import Disc
from data.Pitch import Pitch
from data.Player import Player
import threading
from data.VideoCapture import VideoCapture
from data.VideoCapture2 import VideoCapture2


class Game(object):
    def __init__(self, size):
        pg.init()
        # self.cap = cv2.VideoCapture(0)

        # self.campos = (100,100)
        # self.lastcampos = (100, 100)
        pg.display.set_caption("PyHockey")
        self.screensize = (int(size[0]), int(size[1]))

        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.screen = pg.display.set_mode(self.screensize)

        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 120
        self.keys = pg.key.get_pressed()
        self.done = False

        # model part
        self.pitch = Pitch()
        self.players = [Player(Player.PLAYER_RED, self.pitch), Player(Player.PLAYER_BLUE, self.pitch)]
        self.mallets = [self.players[0].mallet, self.players[1].mallet]
        pitch_borders = [(self.pitch.i_min, self.pitch.i_max), (self.pitch.j_min, self.pitch.j_max)]
        self.discs = [Disc(100, 100, 1, 16.5, pitch_borders), Disc(30, 30, 1, 16.5, pitch_borders)]
        self.objects = self.discs + self.mallets

        # everything that will be drawn
        self.drawables = [self.pitch]
        self.drawables.extend(self.mallets)
        self.drawables.extend(self.discs)

        # self.stop_capture = threading.Event()
        # threading.Thread(target=self.get_image).start()
        self.video = VideoCapture2(size)
        self.video.restart_capture()

        self.loop()

        self.video.stop_capture()


    def loop(self):
        background = (255, 255, 255)
        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True
                    # only for test purposes
                    # elif event.type == pg.MOUSEMOTION:
                    #     self.players[0].mallet.vel.state = event.rel
                    #     self.players[0].mallet.move_to(*event.pos)
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            # reinitialize controls
                            self.video.restart_capture()

            # analyse next frame
            p1_data, p2_data = self.video.getNewPositions()

            # update positions and velocities
            self.players[0].mallet.vel.state, self.players[1].mallet.vel.state = p1_data[1], p2_data[1]

            self.players[0].mallet.move_to(p1_data[0][0], p1_data[0][1])
            self.players[1].mallet.move_to(p2_data[0][0], p2_data[0][1])

            # reset screen
            self.screen.fill(background)

            for o in self.objects:
                o.friction()
                axis = self.pitch.is_border_collision(o)
                if axis:
                    o.border_collision(axis)

            # Detect and react on collisions between discs
            for i in range(len(self.objects) - 1):
                for j in range(i, len(self.objects)):
                    self.objects[i].circle_collision(self.objects[j])

            for disc in self.discs:
                disc.move(disc.vel.x, disc.vel.y)

            # draw everything
            for drawable in self.drawables:
                drawable.draw(self.screen)

            # update display
            pg.display.flip()
            # self.lastcampos = self.campos
