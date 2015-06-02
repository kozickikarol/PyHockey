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
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False

        # model part
        self.pitch = Pitch()
        self.players = [Player(Player.PLAYER_RED, self.pitch), Player(Player.PLAYER_BLUE, self.pitch)]
        self.mallets = [self.players[0].mallet, self.players[1].mallet]
        pitch_borders = [(self.pitch.i_min, self.pitch.i_max), (self.pitch.j_min, self.pitch.j_max)]
        self.discs = [Disc(100, 100, 1, 16.5, pitch_borders), Disc(30, 30, 1, 16.5, pitch_borders)]
        self.objects = self.discs+self.mallets

        # everything that will be drawn
        self.drawables = [self.pitch]
        self.drawables.extend(self.mallets)
        self.drawables.extend(self.discs)

        # self.stop_capture = threading.Event()
        # threading.Thread(target=self.get_image).start()
        # self.video = VideoCapture(self.players[0], self.players[1])
        self.BLUE_video = VideoCapture(self.players[1])
        # self.video.start_capture()
        self.BLUE_video.start_capture()
        self.loop()
        # self.video.stop_capture()
        self.BLUE_video.stop_capture()
        # self.stop_capture.set()
        cv2.destroyAllWindows()

    # def get_image(self):
    #     while not self.stop_capture.is_set():
    #         _, frame = self.cap.read()
    #         frame = cv2.flip(frame, 1)
    #         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #         lower_blue = np.array([90, 80, 80], dtype=np.uint8)
    #         upper_blue = np.array([110,255,255], dtype=np.uint8)
    #         mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #         res = cv2.bitwise_and(frame, frame, mask=mask)
    #         imgray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    #         imgray = cv2.medianBlur(imgray, 5)
    #         contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #         if len(contours):
    #             cnt = contours[0]
    #             (x,y),radius = cv2.minEnclosingCircle(cnt)
    #             center = (int(x),int(y))
    #             self.campos = center
    #             radius = int(radius)
    #             cv2.circle(frame,center,radius,(255,0,0), 2)
    #         cv2.imshow('frame', frame)
    #         k = cv2.waitKey(30)

    def loop(self):
        background = (255, 255, 255)
        while not self.done:
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.done = True
                #only for test purposes
                # elif event.type == pg.MOUSEMOTION:
                #     self.players[0].mallet.vel.state = event.rel
                #     self.players[0].mallet.move_to(*event.pos)

            # self.players[0].mallet.vel.state, self.players[1].mallet.vel.state = self.video.vel
            self.players[1].mallet.vel.state = self.BLUE_video.vel
            # pos = self.video.pos
            pos = self.BLUE_video.pos
            self.players[1].mallet.move_to(pos[0], pos[1])
            # self.players[0].mallet.move_to(pos[0][0], pos[0][1])
            # self.players[1].mallet.move_to(pos[1][0], pos[1][1])
            # dummy line to check if it actually works
            # self.players[0].mallet.position.move(5, 0)

            # reset screen
            self.screen.fill(background)

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
            # self.lastcampos = self.campos