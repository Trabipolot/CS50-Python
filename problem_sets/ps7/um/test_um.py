from um import count


def test_beginning():
    assert count("Um, what do you mean by album?") == 1


def test_multiple():
    assert count("Um, I didn't um know what to um, say to him") == 3


def test_solo():
    assert count("um") == 1


def test_words():
    assert count("Umbilical cords are a dumb way to find your baby's rectum") == 0
