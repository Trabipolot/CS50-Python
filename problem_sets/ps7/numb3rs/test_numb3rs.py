from numb3rs import validate

def test_valid():
    assert validate("111.1.23.255") == True

def test_high():
    assert validate("111.1.23.257") == False

def test_letters():
    assert validate("111.1.23.2l7") == False

def test_digits():
    assert validate("1112.1.23.257") == False

