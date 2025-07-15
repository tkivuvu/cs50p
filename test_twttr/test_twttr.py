from twttr import shorten

def test_argument():
    assert shorten("Thibault") == "Thblt"
def test_argument2():
    assert shorten("DAvId") == "Dvd"
def test_argument3():
    assert shorten("What's your name?") == "Wht's yr nm?"
def test_argument4():
    assert shorten("CS50") == "CS50"

