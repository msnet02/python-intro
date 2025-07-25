# Programa: for-else.py
# Creación: 18/07/2025

# Class definition
class DriveException(Exception):
    pass

# Main code
people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print(person)
        break
else:
    raise DriveException('Driver not found.')
