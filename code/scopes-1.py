# Programa: scopes-1.py
# Actualización: 22/06/2025

# Local versus Global

# We define a function, called local
def local():
    m = 7
    print(m)

# Main code
m = 5
print(m)

# We call, or 'execute' the function local
local()
