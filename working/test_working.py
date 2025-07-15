from working import convert
import pytest

def test_argument1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_argument2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_argument3():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
def test_argument4():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
def test_argument5():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
def test_argument6():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
