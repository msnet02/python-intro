# Programa: scopes-2.py
# Creación: 22/06/2025

# Local versus Global

def local():
    # m doesn't belong to the scope defined by the local function
    # so Python will keep looking into the next enclosing scope.
    # m is finally found in the global scope
    print(m, 'printing from the local scope')

# Main code
m = 5
print(m, 'printing from the global scope')

local()
