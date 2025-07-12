# Programa: ternary.py
# Creación: 09/07/2025

# Main code
order_total = 100

# Classic if/else form
if order_total > 100:
    discount = 25
else:
    discount = 0
print(f"Orden total: {order_total} | Descuento: {discount}")

# Ternary operator
discount = 25 if order_total > 100 else 0
print(f"Orden total: {order_total} | Descuento: {discount}")
