# Programa: primes-2.py
# Creación: 18/07/2025

# Main code: nicer than primes-1.py
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)
