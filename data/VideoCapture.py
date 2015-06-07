from __future__ import division
import threading
import cv2
import numpy as np
from data.Player import Player

class VideoCapture:

    def __init__(self, player, player2=None):
        self.player = player
        self.player2 = None
        self.data = dict()
        self.frame = None

        self.data[player.player_id] = {
            'pos': self.player.mallet.pos.state,
            'last_pos': self.player.mallet.pos.state,
            'vel': (0, 0)
        }
        if player2:
            self.player2 = player2
            self.data[player2.player_id] = {
                'pos': self.player2.mallet.pos.state,
                'last_pos': self.player2.mallet.pos.state,
                'vel': (0, 0)
            }

        self.set_color_mask()
        self._stop_capture = threading.Event()
        self._stop_image_processing = threading.Event()

    def set_color_mask(self):
        if self.player.playerColor == Player.PLAYER_BLUE:
            self.data[self.player.playerColor]['lower'] = np.array([90, 80, 80], dtype=np.uint8)
            self.data[self.player.playerColor]['upper'] = np.array([110, 255, 255], dtype=np.uint8)
            self.data[self.player.playerColor]['circle_color'] = (255, 0, 0)
        else:
            #TODO Provide red mask
            self.data[self.player.playerColor]['lower'] = np.array([90, 80, 80], dtype=np.uint8)
            self.data[self.player.playerColor]['upper'] = np.array([110, 255, 255], dtype=np.uint8)
            self.data[self.player.playerColor]['circle_color'] = (0, 0, 255)
        if self.player2:
            if self.player2.playerColor == Player.PLAYER_BLUE:
                self.data[self.player2.playerColor]['lower'] = np.array([90, 80, 80], dtype=np.uint8)
                self.data[self.player2.playerColor]['upper'] = np.array([110, 255, 255], dtype=np.uint8)
                self.data[self.player2.playerColor]['circle_color'] = (255, 0, 0)
            else:
                #TODO Provide red mask
                self.data[self.player2.playerColor]['lower'] = np.array([90, 80, 80], dtype=np.uint8)
                self.data[self.player2.playerColor]['upper'] = np.array([110, 255, 255], dtype=np.uint8)
                self.data[self.player2.playerColor]['circle_color'] = (0, 0, 255)

    def get_image(self):
        cap = cv2.VideoCapture(0)
        while not self._stop_capture.is_set():
            _, self.frame = cap.read()
            self.frame = cv2.resize(cv2.flip(self.frame, 1), (800, 600))
            for player_id in self.data.keys():
                cv2.circle(self.frame, self.data[player_id]['pos'], 10, self.data[player_id]['circle_color'], 2)
            cv2.imshow('frame', self.frame)
            k = cv2.waitKey(10)

    def get_players_data(self, player_id):
        while not self._stop_image_processing.is_set():
            frame = self.frame
            if frame is None:
                continue
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            self.data[player_id]['last_pos'] = self.data[player_id]['pos']
            mask = cv2.inRange(hsv, self.data[player_id]['lower'], self.data[player_id]['upper'])
            res = cv2.bitwise_and(frame, frame, mask=mask)
            imgray = cv2.medianBlur(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 5)
            contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours):
                cnt = contours[0]
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                self.data[player_id]['pos'] = (int(x), int(y))
                self.data[player_id]['vel'] = (int(x) - self.data[player_id]['last_pos'][0])/10, (int(y) - self.data[player_id]['last_pos'][1])/10
                radius = int(radius)
                # cv2.circle(frame, center, radius, self.data[player_id]['circle_color'], 2)
            else:
                self.data[player_id]['vel'] = (0, 0)

    # def get_image(self):
    #     while not self._stop_capture.is_set():
    #         _, self.frame = self.cap.read()
    #         self.frame = cv2.flip(self.frame, 1)
    #         self.frame = cv2.resize(self.frame, (800, 600))
    #         hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
    #         for player_id in self.data.keys():
    #             self.data[player_id]['last_pos'] = self.data[player_id]['pos']
    #             mask = cv2.inRange(hsv, self.data[player_id]['lower'], self.data[player_id]['upper'])
    #             res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
    #             imgray = cv2.medianBlur(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 5)
    #             contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #             if len(contours):
    #                 cnt = contours[0]
    #                 (x, y), radius = cv2.minEnclosingCircle(cnt)
    #                 center = (int(x), int(y))
    #                 self.data[player_id]['pos'] = center
    #                 self.data[player_id]['vel'] = (int(x) - self.data[player_id]['last_pos'][0])/10, (int(y) - self.data[player_id]['last_pos'][1])/10
    #                 radius = int(radius)
    #                 cv2.circle(self.frame, center, radius, self.data[player_id]['circle_color'], 2)
    #             else:
    #                 self.data[player_id]['vel'] = (0, 0)
    #         cv2.imshow('frame', self.frame)
    #         k = cv2.waitKey(10)

    def start_capture(self):
        threading.Thread(target=self.get_image).start()

    def start_image_processing(self, player):
        threading.Thread(target=self.get_players_data, args=(player.player_id,)).start()

    def stop_capture(self):
        self._stop_capture.set()

    def stop_image_processing(self):
        self._stop_image_processing.set()

    @property
    def pos(self):
        if self.player2:
            return self.data[self.player.player_id]['pos'], self.data[self.player2.player_id]['pos']
        return self.data[self.player.player_id]['pos']

    @property
    def vel(self):
        if self.player2:
            return self.data[self.player.player_id]['vel'], self.data[self.player2.player_id]['vel']
        return self.data[self.player.player_id]['vel']