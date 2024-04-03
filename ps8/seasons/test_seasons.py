from seasons import get_dob, calculate_minutes, convert_to_words
from datetime import date, datetime, time, timedelta
import sys
import pytest

#test get_dob

def test_format(monkeypatch):
    mock_input = "1989-09-06"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    assert get_dob() == datetime(1989,9,6)

def test_error(monkeypatch):
    mock_input = "faulty input"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    with pytest.raises(SystemExit):
        get_dob()

# test calculates_minutes
        
def test_day():
    yesterday=datetime.combine(date.today(), time()) - timedelta(days=1, minutes=1, seconds= 1)
    assert calculate_minutes(yesterday) == 24 * 60 + 1

# test convert_to_words
    
def test_conversion():
    assert convert_to_words(110) == "One hundred ten"
