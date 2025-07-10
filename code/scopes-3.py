# Programa: scopes-3.py
# Creación: 22/06/2025

# Local, Enclosing and Global

def enclosing_func():
    m = 13
    def local():
        # m doesn't belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time m is found in the enclosing scope
        print(m, 'printing from the local scope')

    # Calling the function local (from enclosing_func() function)
    local()

# Main code
m = 5
print(m, 'printing from the global scope')

# Calling enclosing_func() (from 'Main code')
enclosing_func()
