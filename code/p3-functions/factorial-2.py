# Programa: factorial-2.py
# Creación: 26/07/2025

def factorial(n):
    if n in (0, 1):
        result = 1 # by definition
    else:
        result = n # it's very important for 'result *= k' expression makes sense
        for k in range(2, n):
            result *= k
    return result

# Main code
num = factorial(5)
print(num) # prints: 120
