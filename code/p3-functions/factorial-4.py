# Programa: factorial-4.py
# Creación: 26/07/2025

def factorial(n):
    if n in (0,1):
        return 1 # by definition
    return factorial(n - 1) * n # recursive case

# Main code
num = factorial(5)
print(num) # prints: 120
