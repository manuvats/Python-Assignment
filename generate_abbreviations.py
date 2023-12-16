from clean_string import clean_string 
from position_from_last_space import position_from_last_space 
from calculate_score import calculate_score

"""Generate three-letter abbreviations for a given name."""
def generate_abbreviations(name, values):
    
    #Declaring an empty dictionary. 
    abbreviations = {} 
    
    #Removing all punctuation marks and symbols
    name = clean_string(name)
    
    #Declaring first letter of the abbreviation
    first_letter = name[0].upper() #Converting to uppercase for abbreviation
    
    #Declaring some variables to be used in the loop
    second_letter = ''
    second_letter_position = 0
    second_letter_score = 0
    
    for i in range(1, len(name)-1): #Looping through the letters of each word
        if name[i]!=' ': #Only if the character is not a space, the following statements will be run
            second_letter = name[i].upper()
            second_letter_position = position_from_last_space(name, i) + 1
            second_letter_score = calculate_score(second_letter, second_letter_position, name[i+1]==' ', values) 
            #name[i+1] is a condition to check if the next character of the current element is a space.
            #which tells us if the current element or letter is the last one of the current word.
        else: continue
            
        for j in range(i + 1, len(name)): #Looping to find the 3rd letter of the abbreviation
            if name[j]!=' ': 
                third_letter = name[j].upper()
                
                #Concatenating all letters to create abbreviation
                abbreviation = f"{first_letter}{second_letter}{third_letter}"
                
                third_letter_position = position_from_last_space(name, j) + 1
                
                #Is it the last letter? This is checked ny checking if we encounter a space after the letter
                #or if it is the last letter of the whole name
                is_j_last = True if j==len(name)-1 else (True if name[j+1]==' ' else False) 
                
                third_letter_score = calculate_score(third_letter, third_letter_position, is_j_last, values)
                
                total_score = second_letter_score + third_letter_score #Total score for abbreviation
                abbreviations[abbreviation] = total_score
            else: continue
                
    return abbreviations 