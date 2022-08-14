"""
This example is tooled for Ren'Py 8, Python 3.9, and pytest.
https://happytest.readthedocs.io/en/latest/contents/

pyproject.toml sets default name patterns for files, classes, and functions.

By default:
    - Files: test_*.py
    - Classes: Test*
    - Functions: test_*

To change any test setting, see the pytest documentation and edit pyproject.toml:
https://happytest.readthedocs.io/en/latest/reference/#ini-options-ref

Terminology primer:
    - Fixture: a function that can be named as an argument, and pytest will call
        the fixture function for you and send the value for that function argument.
    - Scope "session": Fixture runs once at the start of the entire test session,
        no matter how many times it's used.
    - Scope "module": Fixture runs once for the python file
    - Scope "function" (or no scope given): Fixture runs once per every use as a
        function argument.
    - Assert: measure the given expression and trigger a test error if the result
        is not True.
"""


import pytest


@pytest.fixture(scope="session")
def the_question() -> None:
    return None


@pytest.fixture
def the_answer() -> int:
    return 42


def test_answer_to_the_universe(the_answer, the_question):
    assert the_answer == 42
    assert the_question is None
