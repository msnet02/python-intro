# Programa: scoping-level-1.py
# Creación: 25/07/2024

def my_function():
    test = 1 # this is defined in the local scope of the function
    print('my_function:', test)

# Main code
test = 0 # this is defined in the global scope
my_function()
print('global:', test)
