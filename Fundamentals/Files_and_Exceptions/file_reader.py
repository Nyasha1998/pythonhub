filename = 'pi_digits.txt'

with open(filename) as file_object:
    #takes each line from the file and stores it in a list
    lines = file_object.readlines()
     
for line in lines:
    print(line.rstrip())