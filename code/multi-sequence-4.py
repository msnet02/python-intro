# Programa: multi-sequence-4.py
# Creación: 12/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function zip(people, ages, pronoums, nationalities)
show_message('Using built-in function zip(people, ages, pronoums, nationalities)')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
pronoums = ['he', 'she', 'he', 'he']
nationalities = ['Belgium', 'Spain', 'England', 'Germany']
for person, age, pronoum, nationality in zip(people, ages, pronoums, nationalities):
    print(f"{person} is {age} years old and {pronoum} was born in {nationality}")
