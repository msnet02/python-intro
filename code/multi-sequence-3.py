# Programa: multi-sequence-3.py
# Creación: 12/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function zip(people, ages)
show_message('Using built-in function zip(people, ages)')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
for person, age in zip(people, ages):
    print(f"{person} is {age} years old")
