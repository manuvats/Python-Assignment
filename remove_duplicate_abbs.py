'''Importing necessary libraries'''

'''Function to remove duplicate abbreviations'''
def remove_duplicate_abbs(names_abbs_dict):
    #Creating empty sets to store unique abbreviaiotns as sets do not allow duplicate values 
    unique_abbs = set()
    abbs_to_remove = set()

    # Iterate through the outer dictionary
    for name, abbs_and_score in names_abbs_dict.items():
        #Check if there are no abbreviations
        if not abbs_and_score: 
            # Iterate through the inner dictionary
            for abb in abbs_and_score:
                # Check if the inner key is already encountered
                if abb in unique_abbs:
                    abbs_to_remove.add(abb)
                else:
                    unique_abbs.add(abb)

    # Remove duplicate inner keys from the entire dictionary
    for name in names_abbs_dict:
        names_abbs_dict[name] = {ab: score for ab, score in names_abbs_dict[name].items() if ab not in abbs_to_remove}

    return names_abbs_dict
