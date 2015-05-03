from data.Kinematics import *
from data.Vector import *

class Disc:
    def __init__(self):
        self.__position = Vector(0, 0)
        # TODO: radius length depends on the Pitch size
        self.__radius = 10
        self.__velocity = Vector(0, 0)
        self.__picture_path = "../resources/graphics/disc.jpg"

    # TODO: Use some drawing to display the picture on a pitch
    # Use position, radius, picture_path
    def display(self):
        pass

    @property
    def position(self):
        return self.__position

    @property
    def velocity(self):
        return self.__velocity

    @property
    def radius(self):
        return self.__radius

    @property
    def picture_path(self):
        return self.__picture_path

    def moveTo(self, x, y):
        self.position.state = (x, y)

    def move(self, x_move, y_move):
        self.position.change_state(x_move, y_move)

    def accelerate(self, v_x_diff, v_y_diff):
        self.velocity.change_state(v_x_diff, v_y_diff)

    @velocity.setter
    def velocity(self, v_x, v_y):
        self.velocity.state = (v_x, v_y)

    def printStatus(self):
        print("Position: " + self.position.x + ", " + self.position.y)
        print("Velocity: " + self.velocity.x + ", " + self.velocity.y)
        print("Velocity value: " + self.velocity.length)