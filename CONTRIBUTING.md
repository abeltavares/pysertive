# Contributing to Pysertive 🌟

Welcome to Pysertive! We're excited to have you contribute. Before you get started, please take a moment to review the following guidelines.

<br>

## Branch Organization 🌲

We will do our best to keep the [`main`](https://github.com/abeltavares/marketpipe/tree/main) branch in good shape, with tests passing at all times. If you're looking for a task to contribute to, check out the [Issues](https://github.com/abeltavares/pysertive/issues) tagged with `ready_for_development`.

<br>

## Reporting Bugs 🐞

If you encounter a problem with MarketPipe, you are welcome to open an issue. Before that, please make sure to check if an issue doesn't already exist.

<br>

## How to Contribute ⚡


1. **Fork the Repository**: Click the "Fork" button in the upper right corner of the repository's page on GitHub.
<br>

2. **Clone the Repository**: Clone your fork of the repository to your local machine using Git:

```bash
git clone https://github.com/your-username/pysertive.git
```
<br>

3. **Pick an Issue**: Check out the [Issues](https://github.com/abeltavares/pysertive/issues) tab and get an issue assigned to you. Simply comment `/assign` on an issue, and our GitHub Action will automatically assign the issue to you.
<br>

4. **Create a Branch**: Create a new branch for your contribution:

```bash
git checkout -b feature/your-feature
```
<br>

5. **Install Dependencies**: Install the necessary dependencies using Poetry. This will also set up pre-commit hooks:

```bash
poetry install
```
<br>

6. **Make Changes**: Make your changes to the project locally on your computer.
<br>

7. **Write Tests**: Ensure that your changes are covered by tests. Add new tests if necessary.
<br>

8. **Run Tests**: Run the tests to ensure that your changes do not break existing functionality:

```bash
poetry run pytest
```
<br>

9. **Run Pre-commit Hooks**: Ensure your code passes all pre-commit hooks. These hooks will automatically check your code for common issues, type hinting and enforce consistent styling:

```bash
poetry run pre-commit run --all-files
```
<br>

10. **Commit Changes**: Commit your changes with a descriptive commit message:

```bash
git commit -m "Add your message here"
```
<br>

11. **Push Changes**: Push your changes to your fork of the repository on GitHub:

```bash
git push origin feature/your-feature
```
<br>


12. **Create Pull Request**: Go to the [pysertive repository](https://github.com/abeltavares/pysertive) on GitHub, and click the "New Pull Request" button. Fill out the necessary information and submit your pull request.

   **Note**: The pull request will be commented with code test coverage results. If the coverage is not 100%, please update the tests to cover the new code.

<br>

## Get Started 🚦


### Prerequisites

Make sure you have the following installed on your machine:
- Python 3.10 or later
- [Poetry](https://python-poetry.org/)

<br>

### Installing Dependencies

To install the necessary dependencies, run the following commands:

```bash
poetry install
```

And setup local pre-commit hooks:

```bash
poetry run pre-commit install
```

<br>

## Contact

If you have any questions or need further assistance, feel free to reach out to us. 

<br>
<br>

Thank you for contributing to Pysertive! Together, we can make this project awesome. Let's create something amazing! ✨