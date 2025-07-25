# Programa: binary-2.py
# Creación: 12/07/2025

# Let's create show_bin_value() function
def show_bin_value(n):
    remainders = []
    while n > 0:
        remainder = n % 2 # remainder of the division by 2
        remainders.append(remainder) # we keep track of remainders
        n //= 2 # we divide n by 2

    # Preparing result as string from reverse order items of remainders list
    result = ''
    for char_result in remainders[::-1]:
        result += str(char_result)
    
    return result # function show_bin_value() returns a string as result

# Main code
value = 39 # Using a positive integer number
print(f"{value} in binary is {show_bin_value(value)}")
