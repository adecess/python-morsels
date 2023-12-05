class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Point(self.x*scalar, self.y*scalar, self.z*scalar)

    __rmul__ = __mul__
  
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)
print(p1)
print(p1 == p2)
p2.x = 4
print(p1 == p2)

