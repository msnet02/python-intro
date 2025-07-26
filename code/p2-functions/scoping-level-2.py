# Programa: scoping-level-2.py
# Creación: 25/07/2025

def outer():
    test = 1 # outer scope

    def inner():
        test = 2 # inner scope
        print('inner:', test)

    inner()
    print('outer:', test)

# Main code
test = 0 # global scope
outer()
print('global:', test)
