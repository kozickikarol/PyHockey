from __future__ import absolute_import
import unittest
import math
from data import Kinematics


class TestKinematics(unittest.TestCase):
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

    def test_point_move(self):
        for tup in self.expected_points:
            t_point = Kinematics.Point(tup[0][0], tup[0][1])
            t_point.move(tup[1][0], tup[1][1])
            result = t_point.x, t_point.y
            self.assertEqual(tup[2], result)

    def test_point_move_to(self):
        for tup in self.expected_points_to:
            t_point = Kinematics.Point(tup[0][0], tup[0][1])
            t_point.moveTo(tup[1][0], tup[1][1])
            result = t_point.x, t_point.y
            self.assertEqual(tup[2], result)

    def test_velocity_change(self):
        for tup in self.expected_points:
            t_velo = Kinematics.Velocity(tup[0][0], tup[0][1])
            t_velo.change(tup[1][0], tup[1][1])
            result = t_velo.v_x, t_velo.v_y
            self.assertEqual(tup[2], result)

    def test_velocity_set_coords(self):
        for tup in self.expected_points_to:
            t_velo = Kinematics.Velocity(tup[0][0], tup[0][1])
            t_velo.setCoords(tup[1][0], tup[1][1])
            result = t_velo.v_x, t_velo.v_y
            self.assertEqual(tup[2], result)

    def test_velocity_value(self):
        for tup in self.expected_velocity_value:
            t_velo = Kinematics.Velocity(tup[0][0], tup[0][1])
            result = t_velo.value()
            self.assertTrue((result - tup[1]) < 1e-6)

if __name__ == '__main__':
    unittest.main()
