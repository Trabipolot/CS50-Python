from fuel import gauge, convert

def test_letter():
    assert convert("x/8") == None

def test_denominator():
    assert convert("2/1") == None

def test_convert():
    assert convert("1/2") == 50

def test_dvision_zero():
    assert convert ("0/0") == None

def test_e():
    assert gauge(1) == "E"

def test_f():
    assert gauge(99) == "F"

def test_percentage():
    assert gauge(50) == "50%"