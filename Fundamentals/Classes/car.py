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
        
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_adometer(23500)
my_used_car.read_adometer()
my_used_car.increment_adometer(100)
my_used_car.read_adometer
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_adometer()