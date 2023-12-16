'''Importing necessary libraries'''
import string #To split the string into words

'''Calculate the score for a letter based on its position and value'''
def calculate_score(letter, letter_position, is_last, values):

    letter = letter.upper()  # Convert letter to uppercase
    if letter_position == 1:
        return 0  # First letter of a word has score 0
    elif is_last:
        if letter == 'E':
            return 20  # Last letter is 'E'
        else:
            return 5  # Other last letters
    else:
        position_value = 1 if letter_position == 2 else (2 if letter_position == 3 else 3) #Position value scores
        
        return position_value + values.get(letter, 0)  #Used get to handle missing letters
