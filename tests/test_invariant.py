import pytest
from pysertive import invariant  # type: ignore


def test_invariant_raises_exception_when_initial_balance_is_negative():
    @invariant(
        lambda self: self.balance >= 0,
        exception_type=RuntimeError,
        message="Initial balance cannot be negative",
    )
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

    with pytest.raises(RuntimeError, match="Initial balance cannot be negative"):
        BankAccount(-100)


def test_invariant_raises_exception_when_balance_is_negative():
    @invariant(
        lambda self: self.balance >= 0,
        exception_type=RuntimeError,
        message="Insufficient funds",
    )
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount

    account = BankAccount(100)
    with pytest.raises(RuntimeError, match="Insufficient funds"):
        account.withdraw(200)


def test_invariant_passes_when_balance_is_non_negative():
    @invariant(
        lambda self: self.balance >= 0,
        exception_type=RuntimeError,
        message="Insufficient funds",
    )
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount

    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(50)
    assert account.balance == 100


def test_invariant_applies_to_all_methods():
    @invariant(lambda self: self.value >= 0)
    class TestClass:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value += 1

        def decrement(self):
            self.value -= 1

    obj = TestClass()
    with pytest.raises(AssertionError):
        obj.decrement()


def test_invariant_applies_to_specific_method():
    class TestClass:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value += 1

        @invariant(lambda self: self.value >= 0)
        def decrement(self):
            self.value -= 1

    obj = TestClass()
    obj.increment()
    obj.value = -100
    with pytest.raises(AssertionError):
        obj.decrement()  # This should raise an AssertionError


def test_invariant_excludes_specific_method():
    @invariant(lambda self: self.value >= 0, exclude=["decrement"])
    class TestClass:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value = -100

        def decrement(self):
            self.value -= 1

    obj = TestClass()
    with pytest.raises(AssertionError):
        obj.increment()
    obj.value = 0  # Reset value to avoid AssertionError
    obj.decrement()  # This should not raise an AssertionError
