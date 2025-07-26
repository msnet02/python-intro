# Programa: filter-lambda-1.py
# Creación: 26/07/2025

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

# Main code
print('Los múltiplos de 5 son:', get_multiples_of_five(50))
