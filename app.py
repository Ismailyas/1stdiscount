# app.py

def calculate_price(price, discount_percent=0):
    discount = price * discount_percent / 100
    print(price - discount)
