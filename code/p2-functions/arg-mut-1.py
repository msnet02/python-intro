# Programa: arg-mut-1.py
# Creación: 26/07/2025

def separador(n):
    print('-' * n)

def func(a=[], b={}):
    print(a)
    print(b)
    separador(6)
    a.append(len(a))
    b[len(a)] = len(a)


# Main code
func()
func()
func()
