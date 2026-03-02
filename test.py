import pytest
from calculator import add, subtract, multiply, divide, square_root, factorial, natural_log, power

# --- Basic Tests ---
def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Error: Division by zero"

def test_square_root():
    assert square_root(16) == 3

def test_factorial():
    assert factorial(5) == 120

def test_log():
    import math
    assert natural_log(math.e) == 1

def test_power():
    assert power(2, 3) == 8