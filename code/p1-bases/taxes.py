# Programa: taxes.py
# Creación: 09/07/2025

# Main code
income = 30000 
if income <= 10000:
    tax_coefficient = 0.0
elif income <= 30000:
    tax_coefficient = 0.2
elif income <= 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print(f"I will pay {income * tax_coefficient} in taxes, having income of {income}")
