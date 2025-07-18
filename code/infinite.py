# Programa: infinite.py
# Creación: 18/07/2025

# Main code
from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')
