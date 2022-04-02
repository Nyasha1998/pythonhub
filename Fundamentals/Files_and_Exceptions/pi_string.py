filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    #takes each line from the file and stores it in a list
    lines = file_object.readlines()
    
pi_string = ''
#create a loop that adds each line of digits to pi_string 
#and removes the newline character from each line.
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
            
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
      