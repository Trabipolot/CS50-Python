from twttr import shorten

def test_Google():
    assert shorten("Google") == "Ggl"

def test_aeiouAEIOU():
    assert shorten("aeiouAEIOU") == ""

def test_special_characters():
    assert shorten(".,-Op01") == ".,-p01"
