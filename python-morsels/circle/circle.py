from math import pi

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError('Radius cannot be negative')

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return pi * self.radius ** 2


