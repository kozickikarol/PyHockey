import pygame


class Drawable:

    def __init__(self, image, imagerect, position):
        """
        :param image: shape or image to be drawn
        :param position: position on screen (of type Point)
        :param imagerect: rectangle of image to be displayed
        """
        self.image = image
        self.position = position

    def draw(self, screen):
        """
        Override if in need

        :param screen: pygame screen instance
        """
        # http://stackoverflow.com/questions/8873219/what-is-a-good-way-to-draw-images-using-pygame
        screen.blit(self.image, self.position.toArray())
