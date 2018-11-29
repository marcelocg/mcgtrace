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
        elif isinstance(other, tuple) and len(other) == 4:
            if other[3] == 0:
                return (self.x + other[0],
                        self.y + other[1],
                        self.z + other[2],
                        self.w + other[3])
            else:
                raise ValueError(
                    "Tuple passed as argument does not represent a Vector.")
        elif isinstance(other, Point):
            raise TypeError(
                "Adding two points makes no sense. Try adding a Vector instead.")
        else:
            raise TypeError(
                "Value is not a Vector or a 4-dimensional tuple")
