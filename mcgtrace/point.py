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
