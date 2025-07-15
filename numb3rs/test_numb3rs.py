from numb3rs import validate

def test_argument1():
    assert validate("1.2.3.4") == True
def test_argument2():
    assert validate("127.0.0.1") == True
def test_argument3():
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
def test_argument4():
    assert validate("275.3.6.28") == False
def test_argument5():
    assert validate("cat") == False
def test_argument6():
    assert validate("255.455.455.455") == False



