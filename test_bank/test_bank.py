from bank import value

def test_argument():
    assert value("Hello") == 0
def test_argument2():
    assert value("hello, newman") == 0
def test_argument3():
    assert value("Hey") == 20
def test_argument4():
    assert value("how you doing?") == 20
def test_argument5():
    assert value("What's happening?") == 100
def test_argument6():
    assert value("rtet tutoep") == 100

