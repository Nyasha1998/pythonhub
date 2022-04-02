import csv

# Get temperatures from file
filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # We call the next() once which returns the next line in
    # the file when passed the reader object.
    # We store the data that is returned in header_row.
    header_row = next(reader)
    
    highs = []
    for row in reader:
        highs.append(row[1])
        
    print(highs)
    
    # We use enumerate on the list to get the index of each item
    # as well as the value.
    #for index, column_header in enumerate(header_row):
     #   print(index, column_header)