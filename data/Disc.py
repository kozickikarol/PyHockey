from data.Kinematics import *

class Disc(PhysicsObject):
    def __init__(self, init_x, init_y, mass, radius):
        super(Disc, self).__init__(init_x, init_y, mass, radius)
        self._picture_path = "../resources/graphics/disc.jpg"

    # TODO: Use some drawing to display the picture on a pitch
    # Use position, radius, picture_path
    def display(self):
        pass

    @property
    def pos(self):
        return self._pos

    @property
    def vel(self):
        return self._vel

    @property
    def radius(self):
        return self._radius

    @property
    def picture_path(self):
        return self._picture_path

    def moveTo(self, x, y):
        self._pos.state = (x, y)

    def move(self, x_move, y_move):
        self._pos.change_state(x_move, y_move)

    def accelerate(self, v_x_diff, v_y_diff):
        self._vel.change_state(v_x_diff, v_y_diff)

    @vel.setter
    def vel(self, vel):
        self._vel.state = vel

    def printStatus(self):
        print("Position: " + self._pos.x + ", " + self._pos.y)
        print("Velocity: " + self._vel.x + ", " + self._vel.y)
        print("Velocity value: " + self._vel.length)