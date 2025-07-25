# Programa: multi-sequence-2.py
# Creación: 12/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function enumerate(people)
show_message('Using built-in function enumerate(people)')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
for position, person in enumerate(people):
    print(f"{person} is {ages[position]} years old")
