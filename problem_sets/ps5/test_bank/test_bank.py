from bank import value


def test_hello():
    assert value("hello") == 0


def test_Hello():
    assert value("Hello") == 0


def test_Hi():
    assert value("Hi") == 20


def test_word():
    assert value("word)") == 100


def test_number():
    assert value("20") == 100


def test_word_hello():
    assert value("Well, hello there") == 100
