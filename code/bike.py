# Let's define the class Bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def drive(self):
        print(f"Bike: {self.colour} | {self.frame_material} - Driving!")

    def brake(self):
        print(f"Bike: {self.colour} | {self.frame_material} - Braking!")

# Main code
# Let's create a couple of intances
bike_one = Bike('Red', 'Carbon fiber')
bike_two = Bike('Blue', 'Steel')

# Let's inspect the objects we have, instances of the Bike class
print(bike_one.colour) # prints: Red
print(bike_one.frame_material) # prints: Carbon fiber
print(bike_two.colour) # prints: Blue
print(bike_two.frame_material) # prints: Steel

# Let's brake!
bike_one.brake() # prints: Bike: Colour | Frame material - Braking!

# Let's drive!
bike_two.drive() # prints: Bike: Colour | Frame material - Driving!
