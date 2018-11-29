import pytest
from mcgtrace.point import Point
from mcgtrace.vector import Vector


class TestVector(object):
    def test_recognizes_a_vector_in_a_tuple(self):
        tup = (1.0, 1.0, 1.0, 0.0)
        assert Vector.tuple_is_vector(tup)

    def test_recognizes_a_vector_in_a_vector_object(self):
        vector = Vector(1.0, 1.0, 1.0)
        assert Vector.object_is_vector(vector)

    def test_malformed_tuple_is_not_a_vector(self):
        tup = (1, 1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_point_tuple_is_not_a_vector(self):
        tup = (1, 1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_incomplete_tuple_is_not_a_vector(self):
        tup = (1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_cretes_a_vector(self):
        vector = Vector(1, 1, 1)
        assert vector.w == 0.0

    def test_vector_as_tuple(self):
        vector = Vector(1, 1, 1)
        assert vector.to_tuple() == (1.0, 1.0, 1.0, 0.0)

    def test_addition_to_point_object(self):
        point = Point(3, -2, 5)
        vector = Vector(-2, 3, 1)
        destination = vector.add(point)
        # a point added to a vector results in a translated point (w=1)
        assert destination.to_tuple() == (1, 1, 6, 1)

    def test_addition_to_vector_object(self):
        v1 = Vector(2, 3, 1)
        v2 = Vector(3, 2, 1)
        vr = v1.add(v2)
        # a point added to a vector results in a resulting vector (w=0)
        assert vr.to_tuple() == (5, 5, 2, 0)

    def test_vector_addition_results_in_new_vector_object(self):
        v1 = Vector(2, 3, 1)
        v2 = Vector(3, 2, 1)
        vr = v1.add(v2)
        assert isinstance(vr, Vector)
        assert vr is not v1

    def test_point_addition_results_in_new_point_object(self):
        starting_point = Point(3, -2, 5)
        vector = Vector(-2, 3, 1)
        destination = vector.add(starting_point)
        assert isinstance(destination, Point)
        assert destination is not starting_point

    def test_tuple_as_point_addition_results_in_new_tuple(self):
        start = (3, -2, 5, 1)  # emulates a Point
        vector = Vector(-2, 3, 1)
        dest = vector.add(start)
        assert isinstance(dest, tuple)
        assert dest is not start

    def test_tuple_as_vector_addition_results_in_new_tuple(self):
        v1 = (3, -2, 5, 0)  # emulates a Vector
        v2 = Vector(-2, 3, 1)
        vr = v2.add(v1)
        assert isinstance(vr, tuple)
        assert vr is not v1

    def test_raises_exception_when_wrong_value_passed(self):
        vector = Vector(-2, 3, 1)
        with pytest.raises(ValueError):
            vector.add((1, 2, 3, 4))  # tuple that is not a Point or a Vector

    def test_raises_exception_when_wrong_type_passed(self):
        vector = Vector(-2, 3, 1)
        with pytest.raises(TypeError):
            vector.add(1)
