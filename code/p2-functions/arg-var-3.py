# Programa: arg-var-3.py
# Creación: 25/07/2025

def kwo1(*a, c):
    print(a, c)

def kwo2(a, b=42, *, c):
    print(a, b, c)

# Main code
print("Llamada de la función kwo1():")
kwo1(1, 2, 3, c=7)       # prints (1, 2, 3) 7
kwo1(c=4)                # prints () 4

print("Llamada de la función kwo2():")
kwo2(3, b=7, c=99)      # prints 3 7 99
kwo2(3, c=13)           # prints 3 42 13
