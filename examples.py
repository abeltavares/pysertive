from pysertive import pre_condition  # type: ignore
from pysertive import post_condition  # type: ignore
from pysertive import invariant  # type: ignore

# Function to check if a number is positive
def is_positive(x):
    return x > 0


# Function to check if a result is not zero
def result_is_not_zero(result):
    return result != 0


# Function to check if a balance is non-negative
def balance_is_non_negative(self):
    return self.balance >= 0


@pre_condition(is_positive, message="Input must be positive")
def square(x):
    return x * x


admin_users = ["Admin1", "Admin2", "Admin3"]  # List of admin users


# Function to check if a user is authorized


def is_authorized(user):
    return user in admin_users


# Function to perform a sensitive operation
@pre_condition(
    is_authorized, exception_type=PermissionError, message="User is not authorized."
)
def sensitive_operation(user):
    # Assume sensitive operations here
    print(f"Sensitive operation performed by {user}")


# Function to check if a result matches an expected output
def expected_output(expected):
    def check(result):
        return result == expected

    return check


# Function to greet the user
@post_condition(
    expected_output("Hello, World!"),
    exception_type=AssertionError,
    message="Unexpected output",
)
def greet():
    return "Hello, World!"


# Function to divide two numbers
@pre_condition(
    lambda a, b: b != 0, exception_type=ValueError, message="Divisor cannot be zero"
)
@post_condition(
    lambda result: result != 0,
    exception_type=ValueError,
    message="Result cannot be zero",
)
def divide(a, b):
    return a / b


# Class to represent a bank account
@invariant(
    balance_is_non_negative, exception_type=RuntimeError, message="Insufficient funds"
)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


if __name__ == "__main__":
    # Example usage of square function
    try:
        print(square(2))  # Works
        print(square(-1))  # Raises ValueError
    except AssertionError as e:
        print(f"Caught an exception: {e}")

    # Example usage of sensitive_operation function
    try:
        sensitive_operation({"User1"})  # Raises PermissionError
    except PermissionError as e:
        print(f"Caught an exception: {e}")

    # Example usage of greet function
    print(greet())  # Works

    # Example usage of divide function
    try:
        print(divide(10, 2))  # Works
        print(divide(10, 0))  # Raises ValueError
    except ValueError as e:
        print(f"Caught an exception: {e}")

    # Example usage of BankAccount class
    account = BankAccount(100)
    account.deposit(50)
    print(account.balance)  # Prints 150
    account.withdraw(50)
    print(account.balance)  # Prints 100
    try:
        account.withdraw(200)  # Raises RuntimeError
    except RuntimeError as e:
        print(f"Caught an exception: {e}")
