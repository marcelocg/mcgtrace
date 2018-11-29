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

    def to_tuple(self):
        return (self.x, self.y, self.z, self.w)