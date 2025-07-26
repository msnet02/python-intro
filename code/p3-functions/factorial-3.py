# Programa: factorial-3.py
# Creación: 26/07/2025

from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)

# Main code
num = factorial(5)
print(num) # prints: 120
