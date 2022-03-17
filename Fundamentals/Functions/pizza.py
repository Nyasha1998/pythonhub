def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperron1')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# the asterisk in the parameter name *toppings tells 
# python to make an empty tuple called toppings and 
# pack whatever values it receives into this tuple
