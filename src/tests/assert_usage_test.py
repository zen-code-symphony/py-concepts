import pytest

from app.assert_usage import subtract


def test_subtracts_b_from_a():
    assert subtract(10, 5) == 5


def test_subtracts_b_greater_than_a_throws_error():
    with pytest.raises(AssertionError):
        subtract(10, 15)
