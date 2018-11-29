from mcgtrace.point import Point


class TestPoint(object):
    def test_recognizes_a_point_in_a_tuple(self):
        tup = (1.0, 1.0, 1.0, 1.0)
        assert Point.tuple_is_point(tup)

    def test_recognizes_a_point_in_a_point_object(self):
        point = Point(1.0, 1.0, 1.0)
        assert Point.object_is_point(point)

    def test_malformed_tuple_is_not_a_point(self):
        tup = (1, 1, 1, 2)
        assert not Point.tuple_is_point(tup)

    def test_incomplete_tuple_is_not_a_point(self):
        tup = (1, 1, 1)
        assert not Point.tuple_is_point(tup)

    def test_cretes_a_point(self):
        point = Point(1, 1, 1)
        assert point.w == 1.0
