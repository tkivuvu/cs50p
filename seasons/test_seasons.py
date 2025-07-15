from seasons import dob
import pytest

def test_argument1():
    assert dob("1999-01-01") == "Thirteen million, two hundred seventy-five thousand, three hundred sixty minutes"
    assert dob("1998-06-20") == "Thirteen million, five hundred fifty-six thousand, one hundred sixty minutes"
def test_argument2():
    with pytest.raises(SystemExit):
        dob("February 6th, 1998")
