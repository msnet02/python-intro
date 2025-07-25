# Programa: multi-sequence-5.py
# Creación: 12/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in function zip(people, ages, pronoums, nationalities) with a variation
show_message('Using built-in function zip(people, ages, pronoums, nationalities) with a variation')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
pronoums = ['he', 'she', 'he', 'he']
nationalities = ['Belgium', 'Spain', 'England', 'Germany']
for data in zip(people, ages, pronoums, nationalities):
    person, age, pronoum, nationality = data
    print(f"{person} is {age} years old and {pronoum} was born in {nationality}")
