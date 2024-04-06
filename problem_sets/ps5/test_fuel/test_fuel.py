from fuel import gauge, convert
import pytest


def test_letter():
    with pytest.raises(ValueError):
        convert("x/8")


def test_denominator():
    with pytest.raises(ValueError):
        convert("2/1")


def test_convert():
    assert convert("1/2") == 50


def test_dvision_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_e():
    assert gauge(1) == "E"


def test_f():
    assert gauge(99) == "F"


def test_percentage():
    assert gauge(50) == "50%"
