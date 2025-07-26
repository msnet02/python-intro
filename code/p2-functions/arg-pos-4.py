# Programa: arg-pos-4.py
# Creación: 25/07/2025

def minimun(*n):
    if n: # n is a tuple; a non-empty collection object returns True
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
    else:
        mn = 'nothing'
    print(f"Minimum value of {n} is {mn}")

# Main code
minimun(1, 3, -7, 9)    # n = (1, 3, -7, 9) - prints Minimum value of (1, 3, -7, 9) is -7
minimun()               # n = () - prints Minimum value of () is nothing
minimun(0)              # n = (0) - prints Minimum value of (0,) is 0
