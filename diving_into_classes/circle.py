from math import pi

class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        
    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return pi * self._radius ** 2

c = Circle(5)
print(c)
print(c.radius)
print(c.diameter)
print(c.area)
