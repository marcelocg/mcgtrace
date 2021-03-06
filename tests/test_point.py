import pytest
from mcgtrace.point import Point
from mcgtrace.vector import Vector


class TestPoint(object):
    # ...............{ Validation methods              }...............
    def test_recognizes_a_point_in_a_point_object(self):
        point = Point(1.0, 1.0, 1.0)
        assert Point.object_is_point(point)

    def test_recognizes_a_point_in_a_tuple(self):
        tup = (1.0, 1.0, 1.0, 1.0)
        assert Point.tuple_is_point(tup)

    def test_malformed_tuple_is_not_a_point(self):
        tup = (1, 1, 1, 2)
        assert not Point.tuple_is_point(tup)

    def test_vector_tuple_is_not_a_point(self):
        tup = (1, 1, 1, 0)
        assert not Point.tuple_is_point(tup)

    def test_incomplete_tuple_is_not_a_point(self):
        tup = (1, 1, 1)
        assert not Point.tuple_is_point(tup)

    # ...............{ Creational meths & constructors }...............
    def test_builds_a_point_from_a_tuple(self):
        point = Point.from_tuple((1, 1, 1))
        assert Point.object_is_point(point)

    def test_creates_a_point_from_coordinates(self):
        point = Point(1, 1, 1)
        assert point.w == 1.0

    # ...............{ Conversion methods              }...............
    def test_point_as_tuple(self):
        point = Point(1, 1, 1)
        assert point.to_tuple() == (1.0, 1.0, 1.0, 1.0)

    # ...............{ O P E R A T I O N S             }...............

    # ...............{ Addition                        }...............
    def test_addition_to_vector_object(self):
        point = Point(3, -2, 5)
        vector = Vector(-2, 3, 1)
        destination = point.add(vector)
        # a point added to a vector results in a translated point (w=1)
        assert destination.to_tuple() == (1, 1, 6, 1)

    def test_vector_addition_results_in_new_point_object(self):
        starting_point = Point(3, -2, 5)
        vector = Vector(-2, 3, 1)
        destination = starting_point.add(vector)
        assert isinstance(destination, Point)
        assert destination is not starting_point

    def test_addition_to_tuple_assumes_adding_a_vector(self):
        # tuple argument assumes a Vector,
        # as point addition makes no sense
        vector = (-2, 3, 1)
        point = Point(3, -2, 5)
        dest = point.add(vector)
        # a point added to a vector results in a translated point
        assert isinstance(dest, Point)
        assert dest is not point
        assert dest.to_tuple() == (1, 1, 6, 1)

    def test_point_addition_raises_type_error(self):
        p1 = Point(-2, 3, 1)
        p2 = Point(3, -2, 5)
        with pytest.raises(TypeError):
            dest = p1.add(p2)  # Adding two Points does not make sense

    def test_tuple_as_point_addition_raises_value_error(self):
        point = Point(-2, 3, 1)
        with pytest.raises(ValueError):
            dest = point.add((3, -2, 5, 1))  # tuple that emulates a Point

    def test_tuple_as_vector_addition_raises_value_error(self):
        point = Point(-2, 3, 1)
        with pytest.raises(ValueError):
            dest = point.add((3, -2, 5, 0))  # tuple that emulates a Vector

    def test_invalid_tuple_addition_raises_value_error(self):
        point = Point(-2, 3, 1)
        with pytest.raises(ValueError):
            point.add((1, 2, 3, 4))  # tuple that is not a Point or a Vector

    def test_addition_invalid_type_argument_raises_type_error(self):
        point = Point(-2, 3, 1)
        with pytest.raises(TypeError):
            point.add(7)  # one can not add a scalar to a point

    # ...............{ Subtraction                     }...............
    def test_subtraction_of_two_points_results_in_a_vector(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        rv = p1.sub(p2)
        assert rv.to_tuple() == (-2, -4, -6, 0)

    def test_subtraction_of_a_vector_from_a_point_results_in_a_point(self):
        p1 = Point(3, 2, 1)
        v1 = Vector(5, 6, 7)
        dp = p1.sub(v1)
        assert dp.to_tuple() == (-2, -4, -6, 1)