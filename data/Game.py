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


class Game(object):
    DISC_RADIUS = 16.5
    INIT_POS_DISC1 = 100
    INIT_POS_DISC2 = 30

    def __init__(self, size):
        pg.init()
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
        self.discs = [Disc(Game.INIT_POS_DISC1, Game.INIT_POS_DISC1, 1, Game.DISC_RADIUS, pitch_borders),
                      Disc(Game.INIT_POS_DISC2, Game.INIT_POS_DISC2, 1, Game.DISC_RADIUS, pitch_borders)]
        self.objects = self.discs + self.mallets
        self.scoreboard = ScoreBoard(self.players[0], self.players[1])

        # everything that will be drawn
        self.drawables = [self.pitch]
        self.drawables.extend(self.mallets)
        self.drawables.extend(self.discs)
        self.drawables.append(self.scoreboard)

        self.video = VideoCapture(self.players[0], self.players[1])
        # self.video = VideoCapture2(size)
        self.video.start_capture()
        self.video.start_image_processing(self.players[0])
        self.video.start_image_processing(self.players[1])
        # self.video.restart_capture()

        self.loop()

        self.video.stop_image_processing()
        self.video.stop_capture()

    def loop(self):
        background = (255, 255, 255)
        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True

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
            self.screen.fill(background)

            #check if the goal was scored
            for pl in self.players:
                for d in self.discs:
                    if pl.goal_to_score.in_goal(d.pos.x, d.pos.y, Game.DISC_RADIUS):
                        pl.addPoint()
                        d.move_to(d.init_x, d.init_y)

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
