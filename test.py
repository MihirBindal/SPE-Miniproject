import pytest
from calculator import square_root, factorial, natural_log, power

def test_square_root():
    assert square_root(16) == 4

def test_factorial():
    assert factorial(5) == 120

def test_log():
    # math.log(e) should be 1
    import math
    assert natural_log(math.e) == 1

def test_power():
    assert power(2, 3) == 8