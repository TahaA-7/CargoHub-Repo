import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)


def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)