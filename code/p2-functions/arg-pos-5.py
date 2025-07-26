# Programa: arg-pos-5.py
# Creación: 25/07/2025

def func(*args):
    print(args)

# Main code
values = (1, 3, -7, 9)
func(values)    # equivalent to: func((1, 3, -7, 9)) - prints ((1, 3, -7, 9),)
func(*values)   # equivalent to: func(1, 3, -7, 9) - prints (1, 3, -7, 9)
