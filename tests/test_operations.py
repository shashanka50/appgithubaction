# from src import operations
from src.math_operations import add,sub,mul

def test_add():
    assert add(2,3) == 5
    assert add(2,-3) == -1
    assert add(-2,-3) == -5
    assert add(1,1) == 2
    assert add(-2,3) == 1

def test_sub():
    assert sub(2,3) == -1
    assert sub(2,-3) == 5
    assert sub(-2,-3) == 1
    assert sub(1,1) == 0
    assert sub(-2,3) == -5

def test_mul():
    assert mul(2,3) == 6
    assert mul(2,-3) == -6
    assert mul(-2,-3) == 6
    assert mul(1,1) == 1
    assert mul(-2,3) == -6