from abc import ABCMeta
import pygame


class Drawable:
    __metaclass__ = ABCMeta

    def __init__(self, shape):
        """

        :param shape: shape or image to be drawn
        """
        self.shape = shape

    def __init__(self, shape, position):
        """

        :param shape: shape or image to be drawn
        :param position: position on screen
        """
        self.shape = shape
        self.position = position


    def draw(self, screen):
        """
        Override if in need

        :param screen: pygame screen instance
        """
        # http://stackoverflow.com/questions/8873219/what-is-a-good-way-to-draw-images-using-pygame
        pygame.draw()
