import mcgtrace.vector


class Point:
    def __init__(self, *tup):
        self.x, self.y, self.z = tup
        self.w = 1.0

    @staticmethod
    def tuple_is_point(tup):
        return len(tup) == 4 and tup[-1] == 1.0

    @staticmethod
    def object_is_point(p):
        return p.w == 1.0

    @staticmethod
    def from_tuple(tup):
        return Point(*tup)

    def to_tuple(self):
        return (self.x, self.y, self.z, self.w)

    def add(self, other):
        if isinstance(other, mcgtrace.vector.Vector):
            return Point(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z)
        elif isinstance(other, tuple):
            if len(other) == 3:
                return Point(self.x + other[0],
                             self.y + other[1],
                             self.z + other[2])
            else:
                raise ValueError(
                    "Tuple argument should have 3 dimensions.")
        else:
            raise TypeError(
                "Argument is not a Vector or a 3-dimensional tuple")

    def sub(self, other):
        if isinstance(other, mcgtrace.vector.Vector):
            return Point(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z)
        elif isinstance(other, Point):
            return mcgtrace.vector.Vector(self.x - other.x,
                                          self.y - other.y,
                                          self.z - other.z)
        else:
            raise TypeError(
                "Argument is neither a Point or a Vector.")
