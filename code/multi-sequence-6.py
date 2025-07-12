# Programa: multi-sequence-6.py
# Creación: 12/07/2025

# Let's create the show_message() function
def show_message(text):
    print(f"{'-' * 3}\n{text}:")

# Main code

# Using built-in while loop just for fun
show_message('Using built-in while loop just for fun')
people = ['Marco', 'Carolina', 'Christian', 'Santiago']
ages = [57, 47, 18, 15]
pronoums = ['he', 'she', 'he', 'he']
nationalities = ['Belgium', 'Spain', 'England', 'Germany']
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    pronoum = pronoums[position]
    nationality = nationalities[position]
    print(f"{person} is {age} years old and {pronoum} was born in {nationality}")
    position += 1
