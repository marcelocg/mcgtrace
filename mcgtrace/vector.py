import math
import mcgtrace.point


class Vector:
    def __init__(self, *tup):
        self.x, self.y, self.z = tup
        self.w = 0.0

    @staticmethod
    def tuple_is_vector(tup):
        return len(tup) == 4 and tup[-1] == 0.0

    @staticmethod
    def object_is_vector(p):
        return p.w == 0.0

    @staticmethod
    def from_tuple(tup):
        return Vector(*tup)

    def to_tuple(self):
        return (self.x, self.y, self.z, self.w)

    def add(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)
        elif isinstance(other, mcgtrace.point.Point):
            return mcgtrace.point.Point(self.x + other.x,
                                        self.y + other.y,
                                        self.z + other.z)
        elif isinstance(other, tuple) and len(other) == 4:
            if other[3] == 0 or other[3] == 1:
                return (self.x + other[0],
                        self.y + other[1],
                        self.z + other[2],
                        self.w + other[3])
            else:
                raise ValueError(
                    "Tuple passed as argument does not represent a Point or a Vector")
        else:
            raise TypeError(
                "Value is not a Vector, a Point or a 4-dimensional tuple")

    def sub(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y,
                          self.z - other.z)
        else:
            raise TypeError(
                "Argument is not a Vector.")

    def opposite(self):
        return Vector(self.x * -1,
                      self.y * -1,
                      self.z * -1)

    def scale(self, factor):
        return Vector(self.x * factor,
                      self.y * factor,
                      self.z * factor)

    def magnitude(self):
        return math.sqrt(self.x ** 2 +
                         self.y ** 2 +
                         self.z ** 2)

#   ... A L I A S E S ...

    def scale_by(self, factor):
        return self.scale(factor)

    def length(self):
        return self.magnitude()

    def len(self):
        return self.magnitude()

    def mag(self):
        return self.magnitude()
