class Car():
    """A simple attempt to represent a cat."""
    
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.adometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_adometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.adometer_reading) + " miles on it.")
        
    def update_adometer(self, mileage):
        """Set the adometer reading to the given value."""
        self.adometer_reading = mileage
        
    def increment_adometer(self, miles):
        """Add the given amount to the adometer reading."""
        self.adometer_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + ".kWH battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        #add an attribute called self.battery
        self.battery = Battery()