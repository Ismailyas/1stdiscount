from app import calculate_price

def test_discount_10_percent():
    assert calculate_price(100,10) == 90

def test_discount_20_percent():
    assert calculate_price(200,20) == 160

def test_no_discount():
    assert calculate_price(100,0) == 100