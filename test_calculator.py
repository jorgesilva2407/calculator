import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (10, 15, 25),
    (0, 0, 0),
    (-1, -1, -2),
    (-1, 1, 0),
    (1, -1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (0, -1, -1),
    (-1, 0, -1),
    (-1, 1, 0),
    (1, -1, 0)
])
def test_add(calculator, x, y, expected):
    assert calculator.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 0),
    (10, 15, -5),
    (0, 0, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (1, -1, 2),
    (1, 0, 1),
    (0, 1, -1),
    (0, -1, 1),
    (-1, 0, -1),
    (-1, 1, -2),
    (1, -1, 2)
])
def test_subtract(calculator, x, y, expected):
    assert calculator.subtract(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 1),
    (10, 15, 150),
    (0, 0, 0),
    (-1, -1, 1),
    (-1, 1, -1),
    (1, -1, -1),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (-1, 1, -1),
    (1, -1, -1)
])
def test_multiply(calculator, x, y, expected):
    assert calculator.multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 1),
    (10, 15, 0.6666666666666666),
    (-1, -1, 1),
    (-1, 1, -1),
    (1, -1, -1),
    (0, 1, 0),
    (0, -1, 0),
    (-1, 1, -1),
    (1, -1, -1)
])
def test_divide(calculator, x, y, expected):
    assert calculator.divide(x, y) == expected

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)