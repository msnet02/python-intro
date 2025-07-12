# Programa: binary-3.py
# Creación: 12/07/2025

# Main code
n = 39 # Using a positive integer number
remainders = []
n_orig = n # keep original value of n for showing result
while n > 0:
    n, remainder = divmod(n, 2) # Example: divmod(39, 2) returns (19, 1) tuple
    remainders.append(remainder)

# reassign the list to its reverse copy and print it
remainders = remainders[::-1]
print(f"{n_orig} in binary is {remainders}")
