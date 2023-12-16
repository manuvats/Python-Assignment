'''Importing necessary libraries'''
import re #To keep only letters and remove any symbols

'''Function to remove punctuation marks and symbols'''
def clean_string(input_string):
    #Remove all apostrophes
    cleaned_string = input_string.replace("'", "")
    
    # Replace symbols with spaces
    cleaned_string = re.sub(r'[^a-zA-Z ]', ' ', cleaned_string)

    # Replace multiple spaces with a single space
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)

    return cleaned_string.strip()  #Remove leading and trailing spaces