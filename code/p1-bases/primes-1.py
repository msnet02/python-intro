# Programa: primes-1.py
# Creación: 18/07/2025

# Main code
primes = [] # this will contain the primes in the end
upto = 100 # the limit, inclusive: we will use as range(2, upto + 1)
for n in range(2, upto + 1):
    is_prime = True # Flag, new at each iteration of outer for
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime: # check on flag
        primes.append(n)
print(primes)
