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

    def test_incomplete_tuple_is_not_a_vector(self):
        tup = (1, 1, 1)
        assert not Vector.tuple_is_vector(tup)

    def test_cretes_a_vector(self):
        vector = Vector(1, 1, 1)
        assert vector.w == 0.0
