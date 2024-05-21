import pytest
from pysertive import post_condition  # type: ignore


def test_post_condition_decorator_with_valid_condition():
    @post_condition(
        lambda x: x > 0, exception_type=ValueError, message="Output must be positive"
    )
    def increment(x):
        return x + 1

    assert increment(0) == 1


def test_post_condition_decorator_with_invalid_condition():
    @post_condition(
        lambda x: x > 0, exception_type=ValueError, message="Output must be positive"
    )
    def decrement(x):
        return x - 1

    with pytest.raises(ValueError, match="Output must be positive"):
        decrement(0)
