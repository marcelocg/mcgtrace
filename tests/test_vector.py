import pytest
import math
from mcgtrace.point import Point
from mcgtrace.vector import Vector


class TestVector(object):
    # ...............{ Validation methods              }...............
    def test_recognizes_a_vector_in_a_vector_object(self):
        vector = Vector(1.0, 1.0, 1.0)
        assert Vector.object_is_vector(vector)

    def test_recognizes_a_vector_in_a_tuple(self):
        tup = (1.0, 1.0, 1.0, 0.0)
        assert Vector.tuple_is_vector(tup)

    def test_malformed_tuple_is_not_a_vector(self):
        tup = (1, 1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_point_tuple_is_not_a_vector(self):
        tup = (1, 1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_incomplete_tuple_is_not_a_vector(self):
        tup = (1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    # ...............{ Creational meths & constructors }...............
    def test_builds_a_vector_from_a_tuple(self):
        point = Vector.from_tuple((1, 1, 1))
        assert Vector.object_is_vector(point)

    def test_creates_a_vector(self):
        vector = Vector(1, 1, 1)
        assert vector.w == 0.0

    # ...............{ Conversion methods              }...............
    def test_vector_as_tuple(self):
        vector = Vector(1, 1, 1)
        assert vector.to_tuple() == (1.0, 1.0, 1.0, 0.0)

    # ...............{ O P E R A T I O N S             }...............

    # ...............{ Addition                        }...............
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
        # a vector added to a vector results in a resulting vector (w=0)
        assert vr.to_tuple() == (5, 5, 2, 0)

    def test_addition_to_tuple_as_vector(self):
        v1 = Vector(2, 3, 1)
        v2 = (3, 2, 1, 0)
        vr = v1.add(v2)
        # a vector added to a vector results in a resulting vector (w=0)
        assert vr == (5, 5, 2, 0)

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

    def test_invalid_tuple_addition_raises_value_error(self):
        vector = Vector(-2, 3, 1)
        with pytest.raises(ValueError):
            vector.add((1, 2, 3, 4))  # tuple that is not a Point or a Vector

    def test_addition_invalid_type_argument_raises_type_error(self):
        vector = Vector(-2, 3, 1)
        with pytest.raises(TypeError):
            # one can not add a scalar to a vector
            vector.add(1)

    # ...............{ Subtraction                     }...............
    def test_subtraction_of_two_vectors_results_in_a_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        rv = v1.sub(v2)
        assert rv.to_tuple() == (-2, -4, -6, 0)

    def test_subtraction_of_a_point_from_a_vector_raises_type_error(self):
        v1 = Vector(3, 2, 1)
        pt = Point(5, 6, 7)
        with pytest.raises(TypeError):
            # subtract a point from a vector makes no sense
            v1.sub(pt)

    # ...............{ Negate / Opposite               }...............
    def test_the_opposite_of_a_vector_is_its_negative(self):
        v1 = Vector(3, 2, 1)
        assert v1.opposite().to_tuple() == (-3, -2, -1, 0)

    def test_vector_scaling(self):
        v1 = Vector(1, -2, 3)
        assert v1.scale(3.5).to_tuple() == (3.5, -7, 10.5, 0)
        assert v1.scale(0.5).to_tuple() == (0.5, -1, 1.5, 0)
        assert v1.scale(-2).to_tuple() == (-2, 4, -6, 0)

    def test_vector_scale_by_alias_is_implemented(self):
        v1 = Vector(1, -2, 3)
        assert v1.scale_by(3.5).to_tuple() == (3.5, -7, 10.5, 0)

    def test_unit_X_vector_has_a_magnitude_of_1(self):
        assert Vector(1, 0, 0).magnitude() == 1

    def test_unit_Y_vector_has_a_magnitude_of_1(self):
        assert Vector(0, 1, 0).magnitude() == 1

    def test_unit_Z_vector_has_a_magnitude_of_1(self):
        assert Vector(0, 0, 1).magnitude() == 1

    def test_arbitrary_vector_has_a_magnitude(self):
        assert Vector(1, 2, 3).magnitude() == math.sqrt(14)
        assert Vector(-1, -2, -3).magnitude() == math.sqrt(14)

    def test_vector_length_alias_is_implemented(self):
        assert Vector(1, 0, 0).length() == 1