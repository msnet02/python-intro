# Programa: any-1.py
# Creación: 12/07/2025

# Main code
items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate to True
found = False # this is called "flag"
for item in items:
    print(f"scanning item: {item}")
    if item:
        found = True # we update the flag
        break # This ends the 'for' loop

if found: # we inspect the flag
    print(f"At least one item evaluates to 'True'")
else:
    print(f"All items evaluate to 'False'")
