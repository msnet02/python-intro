# Programa: arg-all-1.py
# Creación: 26/07/2025

def func(a, b, c=7, *args, **kwargs):
    print('--\nResultado:')
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)

# Main code
func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b')
