# Programa: key-arg-pass-2.py
# Creación: 25/07/2025

def func(x):
    x = 7 # defining a local x,  not changing the global one

# Main code
x = 3
func(x)
print(x) # prints: 3
