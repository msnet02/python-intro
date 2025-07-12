# Programa: multi-sequence-1.py
# Creación: 12/07/2025

# Let's create the show_message() funtion
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function range(len(people))
show_message('Using built-in function range(len(people))')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
for position in range(len(people)):
    print(f"{people[position]} is {ages[position]} years old")
