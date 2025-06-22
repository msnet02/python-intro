# Let's define the class Bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    
    def drive(self):
        print("Driving!")

    def brake(self):
        print("Braking!")

# Main code
# Let's create a couple of intances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# Let's inspect the objects we have, instances of the Bike class
print(red_bike.colour) # prints: Red
print(red_bike.frame_material) # prints: Carbon fiber
print(blue_bike.colour) # prints: Blue
print(blue_bike.frame_material) # prints: Steel

# Let's brake!
red_bike.brake() # prints: Braking!

# Let's drive!
blue_bike.drive() # prints: Driving!
