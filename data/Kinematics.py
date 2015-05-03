from __future__ import division
import math
from data.Vector import Vector

class PhycicsObject(object):
    COEFFICIENT_OF_FRICTION = 0.995

    def __init__(self, x_init, y_init, radius, mass):
        self._pos = Vector(x_init, y_init)
        self._mass = mass
        self._radius = radius
        self._vel = Vector(0, 0)

    #TODO: Add unittests
    def friction(self):
        self._vel.length *= self.COEFFICIENT_OF_FRICTION
        self._vel.length = 0 if self._vel.length < 0.1 else self._vel.length

    # def collision_effect(self):
    #     self.velocity.length *= 0.8

    #TODO: Add unittests
    def border_collision(self, axis):
        from data.Disc import Disc
        from data.Mallet import Mallet
        if isinstance(self, Disc):
            if axis == 'x':
                self._vel.x = -self._vel.x
                #TODO: Collision effect - e.g. decreasing velocity
            if axis == 'y':
                self._vel.y = -self._vel.y
                #TODO: Collision effect - e.g. decreasing velocity
        if isinstance(self, Mallet):
            pass
            #TODO: Add move mallet to pitch

    #TODO: Add unittests
    def circle_collision(self, object):
        from data.Disc import Disc
        if self._pos.get_distance(object.pos) <= self._radius+object.radius:
            vec_pos_diff = object.pos - self._pos
            vec_to = self._vel.projection(vec_pos_diff)
            obj_vec_to = object._vel.projection(vec_pos_diff)

            vec_side = self._vel - vec_to
            obj_vec_side = object._vel - obj_vec_to

            after_vec_to = (vec_to*(self._mass-object._mass) + (2 * object._mass * obj_vec_to))/(self._mass + object._mass)
            after_obj_vec_to = (obj_vec_to*(object._mass - self._mass) + (2 * self._mass * vec_to))/(self._mass + object._mass)

            # Change velocity only if it is Disc
            if isinstance(self, Disc):
                self._vel = after_vec_to + vec_side
            if isinstance(object, Disc):
                object._vel = after_obj_vec_to + obj_vec_side


class Point:
    """Point in 2D"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def moveTo(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    def __init__(self, v_x, v_y):
        self.v_x = v_x
        self.v_y = v_y

    def value(self):
        return math.sqrt(self.v_x ** 2 + self.v_y ** 2)

    def change(self, diff_x, diff_y):
        self.v_x += diff_x
        self.v_y += diff_y

    def setCoords(self, v_x, v_y):
        self.v_x = v_x
        self.v_y = v_y

