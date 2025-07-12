# Programa: simple-for-4.py
# Creación: 12/07/2025

# Let's create the show_message() funtion
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function enumerate(surnames)
show_message('Using built-in function enumerate(surnames)')
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(f"{position} - {surname}")
