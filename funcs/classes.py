# Classes in Python
import math


class Circle(object):
    def __init__(self, radius, coordinates=(0.0, 0.0), name=None):
        self.radius = radius
        self.coordinates = coordinates
        if name is None:
            name = f"Circle o:({coordinates[0]}, {coordinates[1]}) r={radius}"
        self.name = name
        return

    def area(self):
        return self.radius * self.radius * math.pi

    def circumference(self):
        return 2 * self.radius * math.pi

    def info(self):
        print(f"Name: {self.name} ==>")
        print(f"Area: {self.area():0.2f}")
        print(f"Circumference: {self.circumference():0.2f}")
        return

    def increment_radius(self, increment):
        self.radius += increment
        return


def example_circle():
    c1 = Circle(radius=2.0, coordinates=(1.0, 1.0))
    c1.info()

    c2 = Circle(radius=1.0)
    c2.info()

    c3 = Circle(1.3)
    c3.info()
    return


if __name__ == "__main__":
    example_circle()
