# Programa: discount-1.py
# Creación: 12/07/2025

from datetime import date, timedelta

def show_separator():
    print(f"{'-' * 5}")

def show_current_prices(list_products):
    for product in list_products:
        print(f"Official price for sku {product['sku']} is {product['price']}")

# Main code
today = date.today()
tomorrow = today + timedelta(days=1) # today + 1 day is tomorrow

# Data: list of dicts
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50.0},
    {'sku': '3', 'expiration_date': today, 'price': 20.0},
]

# Showing current prices
show_current_prices(products)

# Applying discount for today
show_separator()
for product in products:
    if product['expiration_date'] != today:
        continue # No applying any discounts
    product['price'] *= 0.8 # equivalent to applying 20% discount
    print(f"Price for sku {product['sku']} is now {product['price']}")
