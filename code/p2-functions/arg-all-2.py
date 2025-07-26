# Programa: arg-all-2.py
# Creación: 26/07/2025

def func_with_kwonly(a, b=24, *args, c, d=256, **kwargs):
    print('--\nResultado:')
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)

# Main code
func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')
