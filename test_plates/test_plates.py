from plates import is_valid

def test_argument1():
    assert is_valid("HELLO") == True
def test_argument2():
    assert is_valid("HELLO, WORLD") == False
def test_argument3():
    assert is_valid("GOODBYE") == False
def test_argument4():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("CS05") == False
def test_argument5():
    assert is_valid("76HYU") == False
    assert is_valid("50") == False
    assert is_valid("AAA22A") == False
    assert is_valid("H.Y?,") == False
def test_argument6():
    assert is_valid("0JOHN") == False
    assert is_valid("") == False
    assert is_valid("!@#$%") == False
    assert is_valid("HELL!") == False
