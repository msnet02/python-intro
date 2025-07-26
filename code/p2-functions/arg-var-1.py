# Programa: arg-var-1.py
# Creación: 25/07/2025

def func(**kwargs):
    print(kwargs)

# Main code
# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)             # prints {'a': 1, 'b': 42}
func(**{'a': 1, 'b': 42})   # prints {'a': 1, 'b': 42}
func(**dict(a=1, b=42))     # prints {'a': 1, 'b': 42}
