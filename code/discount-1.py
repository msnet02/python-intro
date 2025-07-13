# Programa: discount-1.py
# Creación: 12/07/2025

from datetime import date, timedelta

def show_title(message):
    print(f"{'-' * 3} {message} {'-' * 3}") # Prints a special title

# Main code
today = date.today()
tomorrow = today + timedelta(days=1) # today + 1 day is tomorrow

# Data: list of dicts
products = [
    {'id_prod': '1', 'expiration_date': today, 'price': 100.0},
    {'id_prod': '2', 'expiration_date': tomorrow, 'price': 50.0},
    {'id_prod': '3', 'expiration_date': today, 'price': 20.0},
]

# Showing current prices
show_title('Original prices')
for product in products:
    print(f"Price for id_prod {product['id_prod']} is {product['price']}")
    
# Applying discount for today
show_title('Prices with discount')
for product in products:
    if product['expiration_date'] != today:
        continue # No applying any discounts: This stops current iteration
    product['price'] *= 0.8 # equivalent to applying 20% discount
    print(f"Price for id_prod {product['id_prod']} is {product['price']}")
