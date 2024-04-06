from jar import Jar
import pytest


def test_init_():
    jar = Jar(21)
    assert jar.capacity == 21


def test_str():
    jar = Jar(20)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(25)


def test_withdraw():
    jar = Jar(20)
    jar.size = 15
    jar.withdraw(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.withdraw(20)
