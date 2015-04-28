from __future__ import absolute_import
import unittest
import math
from data import Disc


class TestDisc(unittest.TestCase):
    expected_points = (((0, 0), (1, 2), (1, 2)),
                       ((0, 0), (1, -2), (1, -2)),
                       ((1, -1), (1, 2), (2, 1)),
                       ((-5, 3), (-2, -1), (-7, 2)))

    expected_points_to = (((0, 0), (1, 2), (1, 2)),
                          ((0, 0), (1, -2), (1, -2)),
                          ((1, -1), (1, 2), (1, 2)),
                          ((-5, 3), (-2, -1), (-2, -1)))

    expected_velocity_value = (((0, 0), 0),
                               ((1, -1), math.sqrt(2)),
                               ((1, 2), math.sqrt(5)),
                               ((100, 80), math.sqrt(16400)))

    def test_move_to(self):
        for tup in self.expected_points_to:
            t_disc = Disc.Disc()
            t_disc.moveTo(tup[0][0], tup[0][1])
            t_disc.moveTo(tup[1][0], tup[1][1])
            result = t_disc.position.x, t_disc.position.y
            self.assertEqual(tup[2], result)

    def test_move(self):
        for tup in self.expected_points:
            t_disc = Disc.Disc()
            t_disc.moveTo(tup[0][0], tup[0][1])
            t_disc.move(tup[1][0], tup[1][1])
            result = t_disc.position.x, t_disc.position.y
            self.assertEqual(tup[2], result)

    def test_velocity_set(self):
        for tup in self.expected_points_to:
            t_disc = Disc.Disc()
            t_disc.velocity = tup[0][0], tup[0][1]
            t_disc.velocity = tup[1][0], tup[1][1]
            result = t_disc.velocity.v_x, t_disc.velocity.v_y
            self.assertEqual(tup[2], result)

    def test_accelerate(self):
        for tup in self.expected_points:
            t_disc = Disc.Disc()
            t_disc.velocity = tup[0][0], tup[0][1]
            t_disc.accelerate(tup[1][0], tup[1][1])
            result = t_disc.velocity.v_x, t_disc.velocity.v_y
            self.assertEqual(tup[2], result)


    def test_print_status(self):
        t_disc = Disc.Disc()
        t_disc.velocity = 3, 4
        t_disc.moveTo(1, 2)



if __name__ == '__main__':
    unittest.main()
