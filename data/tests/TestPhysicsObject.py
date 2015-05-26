import unittest
import random
from data.Kinematics import PhysicsObject
from data.Vector import Vector


class TestPhysicsObject(unittest.TestCase):

    MAX_RANDOM_VELOCITY = 25
    MIN_RANDOM_POSITION = 0
    MAX_RANDOM_POSITION = 100
    MIN_RANDOM_BORDERS = 0
    MAX_RANDOM_BORDERS = 100
    MIN_RANDOM_RADIUS = 0
    MAX_RANDOM_RADIUS = 100

    def test_friction(self):
        po = PhysicsObject(50, 50, 1, 50, [(25, 75), (25, 75)])
        for i in range(0, 1000):
            po.vel = Vector(random.randint(0, self.MAX_RANDOM_VELOCITY), random.randint(0, self.MAX_RANDOM_VELOCITY))
            expected_velocity = po.vel * PhysicsObject.COEFFICIENT_OF_FRICTION \
                if po.vel > PhysicsObject.STOPPING_VELOCITY else 0
            po.friction()
            self.assertEquals(po.vel == expected_velocity)

    def test_collision_effect(self):
        po = PhysicsObject(50, 50, 1, 50, [(25, 75), (25, 75)])
        for i in range(0, 1000):
            po.vel = Vector(random.randint(0, self.MAX_RANDOM_VELOCITY), random.randint(0, self.MAX_RANDOM_VELOCITY))
            expected_velocity = po.vel * PhysicsObject.COEFFICIENT_OF_BORDER_COLLISION
            po.collision_effect()
            self.assertEquals(po.vel == expected_velocity)

    def test_correct_position_in_border(self):
        for i in range(0, 1000):
            po = PhysicsObject( random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION),
                                random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION), 1,
                                random.randint(self.MIN_RANDOM_RADIUS, self.MAX_RANDOM_RADIUS),
                                [(random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)),
                                random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)])
            xmin, xmax = po._borders[0]
            ymin, ymax = po._borders[1]

            po.correct_position_in_borders()
            self.assertTrue(po._pos.x - po._radius >= xmin
                            and po._pos.x + po._radius <= xmax
                            and po._pos.y - po._radius >= ymin
                            and po._pos.y + po._radius <= ymax)

    # TODO
    def test_correct_position_post_collision(self):
        pass

    def test_apply_speed_limit(self):
        from data.Mallet import Mallet
        from data.Disc import Disc
        for i in range(0,1000):
            m = Mallet(random.randint(  self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION),
                                        random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION), 1,
                                        random.randint(self.MIN_RANDOM_RADIUS, self.MAX_RANDOM_RADIUS),
                                        [(random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)),
                                        random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)])
            d = Disc(random.randint(    self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION),
                                        random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION), 1,
                                        random.randint(self.MIN_RANDOM_RADIUS, self.MAX_RANDOM_RADIUS),
                                        [(random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)),
                                        random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)])

            m.correct_position_post_collision(d)
            distance_vector = m.pos - d.pos
            self.assertTrue(distance_vector.length >= m.radius + d.radius)

            m = Mallet(random.randint(  self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION),
                                        random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION), 1,
                                        random.randint(self.MIN_RANDOM_RADIUS, self.MAX_RANDOM_RADIUS),
                                        [(random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)),
                                        random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)])
            d = Disc(random.randint(    self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION),
                                        random.randint(self.MIN_RANDOM_POSITION, self.MAX_RANDOM_POSITION), 1,
                                        random.randint(self.MIN_RANDOM_RADIUS, self.MAX_RANDOM_RADIUS),
                                        [(random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)),
                                        random.randint(self.MIN_RANDOM_BORDERS, self.MAX_RANDOM_BORDERS)])

            d.correct_position_post_collision(m)
            distance_vector = m.pos - d.pos
            self.assertTrue(distance_vector.length >= m.radius + d.radius)

    # TODO
    def test_border_collision(self):
        pass

    # TODO
    def test_circle_collision(self):
        pass


if __name__ == '__main__':
    unittest.main()
