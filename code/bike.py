# Let's define the class Bike
class Bike:
    def __init__(self, name, colour, frame_material):
        self.name = name
        self.colour = colour
        self.frame_material = frame_material

    def browse(self):
        print(f"{self.name}: {self.colour} | {self.frame_material}")

    def drive(self):
        print(f"{self.name} - Driving!")

    def brake(self):
        print(f"{self.name} - Driving!")

# Main code
# Let's create a couple of intances
bike_one = Bike('Lamborgini TX-100', 'Red', 'Carbon fiber')
bike_two = Bike('Ferrari Z-1000x', 'Blue', 'Steel')

# Let's inspect the objects we have, instances of the Bike class
bike_one.browse()
bike_two.browse()

# Let's brake!
bike_one.brake() # prints: Bike name - Braking!

# Let's drive!
bike_two.drive() # prints: Bike name - Driving!
