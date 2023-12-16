'''Importing necessary libraries'''

'''Load letter values from the values.txt file'''
def load_values(filename):  
    values = {}
    with open(filename, 'r') as file:
        for line in file:
            letter, value = line.strip().split()
            values[letter] = int(value)
    return values