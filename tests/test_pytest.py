from src.pytest import A

def test_pytest():
    a = A()
    assert A.x == 1

def test_pytest2():
    assert 2 == 2