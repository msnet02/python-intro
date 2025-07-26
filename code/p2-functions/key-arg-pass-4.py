# Programa: key-arg-pass-3.py
# Creación: 25/07/2025

def func(x):
    x[1] = 42 # this affects the caller!
    x = 'something else' # this points x to a new string object

# Main code
x = [1, 2, 3]
print(x)

func(x)
print(x) # still prints: [1, 42, 3]
