# Programa: simple-for-1.py
# Creación: 11/07/2025

# Let's create the show_message() funtion
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using a list of integer items
show_message('Using a list of integer items')
for number in [0, 1, 2, 3, 4]:
    print(number)

# Using built-it function range(5)
show_message('Using built-it function range(5)')
for number in range(5):
    print(number)

# Using built-it function range(-10, 10, 4)
show_message('Using built-it function range(-10, 10, 4)')
for number in range(-10, 10, 4):
    print(number)
