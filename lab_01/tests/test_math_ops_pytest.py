# lab_01/tests/test_math_ops_pytest.py
import pytest
from mypkg.math_ops import add, sub, mul, div, is_prime

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(10, 4) == 6
    assert sub(-3, -5) == 2

def test_mul():
    assert mul(3, 7) == 21
    assert mul(-2, 5) == -10

def test_div():
    assert div(12, 3) == 4
    assert div(7, 2) == 3.5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (1, False),
        (0, False),
        (18, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected

