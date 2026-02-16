# tests/test_tst.py
from tst import add

def test_add():
    assert add(2, 3) == 5  # this should pass
    assert add(0, 0) == 0  # another simple check
