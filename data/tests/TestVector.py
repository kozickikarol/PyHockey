import unittest
from data import Vector
from math import sqrt
from math import cos
from math import pi
from math import sin


class TestVector(unittest.TestCase):
    init_value = ((1, 1), (-89, 0), (15, 23), (100, 890), (1000, 1001),
                  (200, 300), (-200, -100))
    expected_value = (((2., 0.), 2 * 2 + 0 * 0), ((9., 4.), 9 * 9 + 4 * 4),
                      ((15., 12.), 15 * 15 + 12 * 12), ((58., 32.), 58 * 58 + 32 * 32),
                      ((105., 3.), 105 * 105 + 3 * 3), ((-80., 4.), -80 * -80 + 4 * 4),
                      ((-5., -3.), -5 * -5 + -3 * -3), ((12., 34.), 12 * 12 + 34 * 34),
                      ((15., -30.), 15 * 15 + -30 * -30), ((14., -98.), 14 * 14 + -98 * -98))
    set_value = ((0, (0, 0)), (1, (1, 1)), (5, (4, 4)))
    rotate_value = (((0.1, 0.5), pi/3,
                     Vector.Vector(0.1 * cos(pi/3) - 0.5*sin(pi/3), 0.1 * sin(pi/3) + 0.5 * cos(pi/3))),
                    ((5., 0.2), pi/6,
                     Vector.Vector(5.0 * cos(pi/6) - 0.2*sin(pi/6), 5.0 * sin(pi/6) + 0.2 * cos(pi/6))),
                    ((5.5, 3.2), pi,
                     Vector.Vector(5.5 * cos(pi) - 3.2*sin(pi), 5.5 * sin(pi) + 3.2 * cos(pi))),
                    ((18., 30.42), pi/2,
                     Vector.Vector(18.0 * cos(pi/2) - 30.42*sin(pi/2), 18.0 * sin(pi/2) + 30.42 * cos(pi/2))),
                    ((39.3, 10.2), pi/6,
                     Vector.Vector(39.3 * cos(pi/6) - 10.2 * sin(pi/6), 39.3 * sin(pi/6) + 10.2 * cos(pi/6))),
                    ((15., 52), pi/12,
                     Vector.Vector(15.0 * cos(pi/12) - 52*sin(pi/12), 15.0 * sin(pi/12) + 52 * cos(pi/12))),
                    ((5., 0.2), 2*pi,
                     Vector.Vector(5.0 * cos(2*pi) - 0.2*sin(2*pi), 5.0 * sin(2*pi) + 0.2 * cos(2*pi))))
    dot_value = (((0, 0), (1, 1), 0*1 + 0*1),
                 ((5, 18), (23, 55), 5 * 23 + 18 * 55),
                 ((280, 3), (20, 98), 280 * 20 + 3 * 98),
                 ((34, 12), (18, 44), 34 * 18 + 12 * 44))

    def test_init(self):
        for tup in self.init_value:
            checked_vector = Vector.Vector(tup)
            result = (checked_vector.x, checked_vector.y)
            self.assertEqual(tup, result)
        for tup in self.init_value:
            checked_vector = Vector.Vector(tup[0], tup[1])
            result = (checked_vector.x, checked_vector.y)
            self.assertEqual(tup, result)

    def test_length_sqrd(self):
        for tup in self.expected_value:
            checked_vector = Vector.Vector(tup[0])
            result = checked_vector.length_sqrd
            self.assertEqual(tup[1], result)

    def test_length(self):
        for tup in self.expected_value:
            checked_vector = Vector.Vector(tup[0])
            result = checked_vector.length_sqrd
            self.assertEqual(sqrt(tup[1]), sqrt(result))

    # def test_set_length(self):
    #     for tup in self.set_value:
    #         checked_vector = Vector.Vector(5, 5)
    #         print 'tup:', tup[0]
    #         checked_vector.length(tup[0])
    #         result = (checked_vector.x, checked_vector.y)
    #         self.assertEqual(tup[1], result)

    def test_rotated(self):
        for tup in self.rotate_value:
            checked_vector = Vector.Vector(tup[0])
            result = checked_vector.rotated(tup[1])
            self.assertEqual((tup[2].x, tup[2].y), (result.x, result.y))

    def test_rotate(self):
        for tup in self.rotate_value:
            checked_vector = Vector.Vector(tup[0])
            checked_vector.rotate(tup[1])
            self.assertEqual((tup[2].x, tup[2].y), (checked_vector.x, checked_vector.y))

    # def test_normalized(self):
    #     for tup in self.expected_value:
    #         checked_vector = Vector.Vector(tup[0])
    #         checked_vector.normalized
    #         self.assertEqual(1, checked_vector.length)

    # def test_perpendicular(self):
    #     for tup in self.init_value:
    #         checked_vector = Vector.Vector(tup)
    #         result = checked_vector.perpendicular
    #         print result
    #         self.assertEqual((-tup[0], tup[1]), (result.x, result.y))

    def test_dot(self):
        for tup in self.dot_value:
            checked_vector = Vector.Vector(tup[0])
            helping_vector = Vector.Vector(tup[1])
            result = checked_vector.dot(helping_vector)
            self.assertEqual(tup[2], result)

    def test_get_distance(self):
        for tup in self.dot_value:
            checked_vector = Vector.Vector(tup[0])
            helping_vector = Vector.Vector(tup[1])
            result = checked_vector.get_distance(helping_vector)
            print tup[0], tup[1]
            self.assertEqual(sqrt((tup[0][0] - tup[1][0]) ** 2 + (tup[0][1] - tup[1][1]) ** 2), result)

    def test_change_state(self):
        for tup in self.init_value:
            checked_vector = Vector.Vector(tup)
            checked_vector.change_state(tup)
            self.assertEqual((tup[0]*2, tup[1]*2), (checked_vector.x, checked_vector.y))

    # def test_state(self):
    #     for tup in self.init_value:
    #         checked_vector = Vector.Vector(tup)
    #         print tup
    #         checked_vector.state(tup)
    #         self.assertEqual(tup, (checked_vector.x, checked_vector.y))

if __name__ == '__main__':
    unittest.main()