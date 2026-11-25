# app.py
def calculate_price(price, discount_percent=0):
    discount = price * discount_percent / 100
    return price - discount

if __name__ == "__main__":
    print(calculate_price(100, 10))