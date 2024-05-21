Pysertive ✔️
=========

<p align="center">
    <img src="assets/pysertive.png" alt="Pysertive Logo" width="200" height="200">
</p>

<p align="center">
    <a href="https://github.com/abeltavares/pysertive/releases">
        <img src="https://img.shields.io/github/v/release/abeltavares/pysertive.svg" alt="Latest release">
    </a>
    <a href="https://github.com/abeltavares/pysertive/actions/workflows/unit-tests.yml">
        <img src="https://github.com/abeltavares/pysertive/actions/workflows/unit-tests.yml/badge.svg" alt="build status (GitHub Actions)">
    </a>
    <!-- COVERAGE_BADGE_URL -->
    <a href="https://img.shields.io/badge/coverage-100%25-green">
        <img src="https://img.shields.io/badge/coverage-100%25-green" alt="code coverage">
    </a>
    <!-- END_COVERAGE_BADGE_URL -->
    <a href="https://pypi.python.org/pypi/pysertive">
        <img src="https://img.shields.io/pypi/v/reader.svg" alt="PyPI status">
    </a>
    <a href="http://mypy-lang.org/">
        <img src="http://www.mypy-lang.org/static/mypy_badge.svg" alt="checked with mypy">
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
        <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit enabled">
    </a>
    <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code style: black">
    </a>
</p>

<br>

<div align="center">

**Pysertive**: Assertive Python Design by Contract (DbC) Toolkit

</div>

What is it?
--------

Pysertive is a Python library that provides decorators for implementing Design by Contract (DbC) principles. It simplifies enforcing preconditions, postconditions, and invariants in your code. 
Pysertive aims to be a powerful tool for ensuring code behavior and constraints, promoting secure, maintainable, and robust software development in Python.
## Table of Contents

-   [Features](#features)
-   [Where to get it?](#where-to-get-it)
-  [Quick Start](#quick-start)
- [Usage](#usage)
- [Why Pysertive?](#why-pysertive)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

🌟 Features
--------
The things that Pysertive does well:

-   Preconditions: Ensure that function inputs meet defined criteria before execution.
-   Postconditions: Validate that the function outputs conform to expected conditions after execution.
-   Invariants: Guarantee that certain conditions remain true throughout the lifecycle of class instances.

Pysertive is designed with simplicity and flexibility in mind, allowing you to easily integrate rigorous contract checks into your Python code, which helps in debugging and maintaining complex systems.

📦 Where to get it?
------------

To install Pysertive, simply use pip:

```bash
pip install pysertive
```

🚀 Quick Start
-----------

Here's how to quickly get started with Pysertive:

```python
from pysertive import pre_condition, post_condition, invariant

@pre_condition(lambda x: x > 0, exception_type=ValueError, message="Input must be positive")
def sqrt(x):
    return x ** 0.5

@post_condition(lambda result: result != None, exception_type=AssertionError, message="Result cannot be None")
def fetch_data():
    return {"data": "Here is your data"}

@invariant(lambda self: self.balance >= 0, exception_type=RuntimeError, message="Insufficient funds")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount  # No need to manually check for negative balance
```

🔧 Usage
-----

### Using Preconditions

Ensure inputs to your functions are valid:

```python
@pre_condition(lambda age: age >= 18, exception_type=ValueError, message="Must be 18 or older")
def sign_contract(age):
    print(f"Contract signed by individual aged {age}")
```

### Using Postconditions

Validate outputs after your functions execute:

```python
@post_condition(lambda result: result > 0, exception_type=AssertionError, message="Profit must be positive")
def calculate_profit(revenue, costs):
    return revenue - costs
```

### Using Invariants

Enforce class states remain consistent:

```python
@invariant(lambda self: self.inventory_count >= 0, exception_type=RuntimeError, message="Inventory count cannot be negative")
class Warehouse:
    def __init__(self, inventory_count):
        self.inventory_count = inventory_count

    def add_stock(self, number):
        self.inventory_count += number

    def remove_stock(self, number):
        self.inventory_count -= number
```

❓ Why Pysertive?
--------------

-   Reliability: Enforce rules consistently across your application.
-   Maintainability: Easier to manage and update code with clear contractual obligations.
-   Security: Prevents unexpected behaviors by strictly checking function inputs and outputs.

## 📚 Examples

For more detailed examples of how to use Pysertive, check out the `examples.py` file in the repository. This file contains examples of how to use preconditions, postconditions, and invariants in your Python code.

🤝 Contributing
------------

Contributions are welcome! If you'd like to contribute, please check out the [Contributing Guide](CONTRIBUTING.md), and feel free to open an issue or a pull request.

📜 License
-------

Pysertive is released under the MIT License. See the [License](LICENSE.txt) file for more details.

<hr>

[Go to Top](#table-of-contents)