# Programa: simple-for-2.py
# Creación: 11/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-it function range(len(surnames))
show_message('Using built-it function range(len(surnames))')
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(f"{position} - {surnames[position]}")
