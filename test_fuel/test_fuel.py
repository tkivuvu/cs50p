

from fuel import convert, gauge
import pytest

def test_argument1():
    assert convert("1/4") == 25
def test_argument2():
    assert gauge(1) == "E"
def test_argument3():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_argument4():
    with pytest.raises(ValueError):
        convert("cat")
def test_argument5():
    with pytest.raises(ValueError):
        convert("5/4")
def test_argument6():
    assert gauge(99) == "F"
def test_argument7():
    assert gauge(75) == "75%"
