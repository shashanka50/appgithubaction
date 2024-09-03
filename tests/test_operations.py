# from src import operations
from src.math_operations import add,sub

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