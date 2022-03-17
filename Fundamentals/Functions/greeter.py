def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('nyasha')

def display_message(topic):
    print("Hie everyone in this chapter we are learning " + topic.title())
    
display_message("functions")

#Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('Jimi', 'dludlu')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

