from plates import is_valid

def test_letters_only():
    assert is_valid("ABCDEF") is True

def test_letters_digits():
    assert is_valid("ABC123") is True

def test_numbers_only():
    assert is_valid("123456") is False

def test_digit_after_number():
    assert is_valid("AB123Z") is False

def test_too_long():
    assert is_valid("ABC1234") is False

def test_too_short():
    assert is_valid("A") is False

def test_two_chars():
    assert is_valid("AB") is True

def test_four_chars():
    assert is_valid("ABC1") is True

def test_first_two_letters():
    assert is_valid("A1234") is False

def test_special_chars():
    assert is_valid("AB.123") is False

