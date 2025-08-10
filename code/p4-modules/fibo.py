# Programa: fibo.py
# Creación: 09/08/2025

""" Sucesión de Fibonacci: Usar desde el intérprete de Python."""

def fibo1(n):
    """Función que muestra la Sucesión de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print() # Genera un salto de línea al final

def fibo2(n):
    """Función que devuelve la Sucesión de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
