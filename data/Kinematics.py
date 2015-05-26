from __future__ import division
import math
from data.Vector import Vector


class PhysicsObject(object):
    COEFFICIENT_OF_FRICTION = 0.99
    COEFFICIENT_OF_BORDER_COLLISION = 0.8
    MAX_MALLET_VELOCITY = 25
    MAX_DISC_VELOCITY = 50
    STOPPING_VELOCITY = 0.1

    def __init__(self, x_init, y_init, mass, radius, borders):
        self._pos = Vector(x_init, y_init)
        self._mass = mass
        self._radius = radius
        self._vel = Vector(0, 0)
        self._borders = borders

    # TODO: Add unittests
    def friction(self):
        self._vel.length *= self.COEFFICIENT_OF_FRICTION
        self._vel.length = 0 if self._vel.length < STOPPING_VELOCITY else self._vel.length

    def collision_effect(self):
        # TODO: a proper calculation of momentum and change in speed after collisions
        self._vel.length *= self.COEFFICIENT_OF_BORDER_COLLISION

    def correct_position_in_borders(self):
        """ Dislodges objects stuck in the pitch borders """
        x_min, x_max = self._borders[0]
        y_min, y_max = self._borders[1]
        if self.pos.x - self.radius < x_min:
            self.pos.x = x_min+self.radius
        if self.pos.x + self.radius > x_max:
            self.pos.x = x_max-self.radius
        if self.pos.y - self.radius < y_min:
            self.pos.y = y_min+self.radius
        if self.pos.y + self.radius > y_max:
            self.pos.y = y_max-self.radius

    def correct_position_post_collision(self, obj):
        """ Dislodges objects stuck in each other. """
        distance_vector = self.pos - obj.pos

        if distance_vector.length < self.radius + obj.radius:
            distance_vector.length = self.radius + obj.radius
            self._pos = obj.pos + distance_vector
            self.correct_position_in_borders()

        distance_vector = obj.pos - self.pos

        if distance_vector.length < obj.pos - self.pos:
            distance_vector.length = self.radius + obj.radius
            obj._pos = self._pos + distance_vector
            obj.correct_position_in_borders()

    # TODO: Add common move_to and move methods for mallet and disc

    def apply_speed_limit(self):
        from data.Disc import Disc
        from data.Mallet import Mallet
        if isinstance(self, Disc) and self._vel.length > self.MAX_DISC_VELOCITY:
            self._vel.length = self.MAX_DISC_VELOCITY
        if isinstance(self, Mallet) and self._vel.length > self.MAX_MALLET_VELOCITY:
            self._vel.length = self.MAX_MALLET_VELOCITY

    # TODO: Add unittests
    def border_collision(self, axis):
        from data.Disc import Disc
        if isinstance(self, Disc):
            if axis == 'x':
                self._vel.x = -self._vel.x
                self.collision_effect()
                self.correct_position_in_borders()
            if axis == 'y':
                self._vel.y = -self._vel.y
                self.collision_effect()
                self.correct_position_in_borders()

    # TODO: Add unittests
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

            self.apply_speed_limit()
            self.correct_position_post_collision(object)
