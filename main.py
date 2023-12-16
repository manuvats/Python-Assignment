'''Importing necessary functions'''
from load_values import load_values
from generate_abbreviations import generate_abbreviations
from remove_duplicate_abbs import remove_duplicate_abbs 
from keep_min_score import keep_min_score

'''Main function'''
def main():
    #Getting input file and output filename
    input_filename = input("Enter the input filename (e.g., names.txt): ")
    output_filename = input("Enter your surname (for output filename): ").lower() + f"_{input_filename}_abbrevs.txt"

    #Loading the contents of values file
    values = load_values("values.txt")
    
    #Empty dictionary for all abbreviations
    all_abbreviations = {}

    #Opening the input file in read mode and output file in write mode
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        
        for line in input_file:
            name = line.strip() #Splitting each line into names
            
            abbreviations = generate_abbreviations(name, values)
            if not abbreviations:
                output_file.write('\n')  #No abbreviation found for the name
            else:
                best_abbreviation, best_score = min(abbreviations.items(), key=lambda x: x[1])
                #This line finds out the abbreviation with min score with its score
                #Uses the min function where key is the argument based on which the min value will be found
                #Here key will be the score of each abbreviation which is value part of the pair in the abbreviation set.
                
                #Storing all abbreviations in the dictionary
                all_abbreviations[name] = abbreviations
                
                #Removing duplicate abbreviations
                all_abbbreviations = remove_duplicate_abbs(all_abbreviations)
                
        #Keeping abbreviations with minimum scores
        all_abbreviations = keep_min_score(all_abbreviations)
        
        #Writing the abbreviations beside the name in a file
        for key_name in all_abbreviations:
            output_file.write(key_name + ' | ')
            output_file.write(' '.join(all_abbreviations[key_name]) + '\n') #Joining the best abbreviations
        print("Output file " + output_filename + " successfully created")

if __name__ == "__main__":
    main()
