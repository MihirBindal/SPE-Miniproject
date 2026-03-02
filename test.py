import pytest
import math
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(6, 5) == 11.0

def test_divide():
    assert calc.divide(6, 3) == 2.0
    with pytest.raises(ValueError, match="Error! Division by zero."):
        calc.divide(1, 0)

def test_square_root():
    assert calc.square_root(16) == 4.0
    with pytest.raises(ValueError, match="Error! Square root of a negative number."):
        calc.square_root(-1)

def test_factorial():
    assert calc.factorial(5) == 120
