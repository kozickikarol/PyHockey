from __future__ import division

import os
import pygame as pg
from pygame.locals import *
from data.Disc import Disc
from data.Pitch import Pitch
from data.Player import Player

from data.ScoreBoard import ScoreBoard
from data.VideoCapture import VideoCapture
from data.VideoCapture2 import VideoCapture2
from Logger import Logger


class Game(object):
    def __init__(self, size):
        Logger.info("GAME INIT: Initializing PyGame...")
        pg.init()

        Logger.info("GAME INIT: Initializing Display (%s)", str(size))
        pg.display.set_caption("PyHockey")
        self.screensize = (int(size[0]), int(size[1]))

        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.screen = pg.display.set_mode(self.screensize)

        self.screen_rect = self.screen.get_rect()
        Logger.info("GAME INIT: Initializing clock and fps rate...")

        self.clock = pg.time.Clock()
        self.fps = 120
        self.keys = pg.key.get_pressed()
        self.done = False


        Logger.info("GAME INIT: Initializing Model...")
        # model part
        self.pitch = Pitch()
        self.players = [Player(Player.PLAYER_RED, self.pitch), Player(Player.PLAYER_BLUE, self.pitch)]
        self.mallets = [self.players[0].mallet, self.players[1].mallet]
        pitch_borders = [(self.pitch.i_min, self.pitch.i_max), (self.pitch.j_min, self.pitch.j_max)]
        self.discs = [Disc(100, 100, 1, 16.5, pitch_borders), Disc(30, 30, 1, 16.5, pitch_borders)]
        self.objects = self.discs + self.mallets
        self.scoreboard = ScoreBoard(self.players[0], self.players[1])

        Logger.info("GAME INIT: Initializing Drawables...")
        # everything that will be drawn
        self.drawables = [self.pitch]
        self.drawables.extend(self.mallets)
        self.drawables.extend(self.discs)
        self.drawables.append(self.scoreboard)

        Logger.info("GAME INIT: Initializing Video Capture...")
        self.video = VideoCapture(self.players[0], self.players[1])
        # self.video = VideoCapture2(size)
        self.video.start_capture()
        self.video.start_image_processing(self.players[0])
        self.video.start_image_processing(self.players[1])
        # self.video.restart_capture()

        Logger.info("GAME INIT: Starting game loop...")
        self.loop()
        Logger.info("GAME INIT: Game loop ended, stopping video capture...")
        self.video.stop_image_processing()
        self.video.stop_capture()
        Logger.info("GAME INIT: Exiting")

    def loop(self):
        background = (255, 255, 255)
        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    Logger.info("Quit event registered")
                    self.done = True

            Logger.info("GAME LOOP: Setting mallet initial state")
            self.players[0].mallet.vel.state, self.players[1].mallet.vel.state = self.video.vel
            pos = self.video.pos
            # analyse next frame
            # p1_data, p2_data = self.video.getNewPositions()

            self.players[0].mallet.move_to(pos[0][0], pos[0][1])
            self.players[1].mallet.move_to(pos[1][0], pos[1][1])

            # update positions and velocities
            # self.players[0].mallet.vel.state, self.players[1].mallet.vel.state = p1_data[1], p2_data[1]
            #
            # self.players[0].mallet.move_to(p1_data[0][0], p1_data[0][1])
            # self.players[1].mallet.move_to(p2_data[0][0], p2_data[0][1])

            # reset screen
            Logger.info("GAME LOOP: Resetting screen")
            self.screen.fill(background)

            Logger.info("GAME LOOP: Calculating friction and collisions")
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

            Logger.info("GAME LOOP: Draw objects")
            # draw everything
            for drawable in self.drawables:
                drawable.draw(self.screen)

            # update display
            pg.display.flip()
