# Programa: scoping-level-4.py
# Creación: 25/07/2025

def outer():
    test = 1 # outer scope

    def inner():
        global test
        test = 2 # global scope
        print('inner:', test)
    
    inner()
    print('outer', test)

# Main code
test = 0 # global scope
outer()
print('global:', test)
