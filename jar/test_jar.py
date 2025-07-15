from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.capacity = -1

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"





