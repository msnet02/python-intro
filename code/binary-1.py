# Programa: binary-1.py
# Creación: 12/07/2025

# Main code
n = 39 # Using a positive integer number
remainders = []
n_orig = n # keep original value of n for showing result
while n > 0:
    remainder = n % 2 # remainder of the division by 2
    remainders.append(remainder) # we keep track of remainders
    n //= 2 # we divide n by 2

# reassign the list to its reverse copy and print it
remainders = remainders[::-1]
print(f"{n_orig} in binary is {remainders}")
