from um import count

def test_argument1():
    assert count("um") == 1
def test_argument2():
    assert count("Hello, um, world") == 1
def test_argument3():
    assert count("This is, um... CS50") == 1
def test_argument4():
    assert count("Um... what are regular expressions") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
