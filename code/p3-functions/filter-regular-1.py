# Programa: filter-regular-1.py
# Creación: 26/07/2025

def is_multiple_of_five(n):
    return not n % 5 # if n is multuple of five returns "not False" -> True

def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))

# Main code
print('Los múltiplos de 5 son:', get_multiples_of_five(50))
