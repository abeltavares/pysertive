import pytest
from pysertive import pre_condition  # type: ignore


def test_pre_condition_decorator_with_valid_condition():
    @pre_condition(
        lambda x: x > 0, exception_type=ValueError, message="Input must be positive"
    )
    def increment(x):
        return x + 1

    assert increment(1) == 2


def test_pre_condition_decorator_with_invalid_condition():
    @pre_condition(
        lambda x: x > 0, exception_type=ValueError, message="Input must be positive"
    )
    def increment(x):
        return x + 1

    with pytest.raises(ValueError, match="Input must be positive"):
        increment(-1)
