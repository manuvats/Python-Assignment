'''Importing necessary libraries'''

'''Function for keeping the abbreviations with minimum scores '''
def keep_min_score(names_abbs_dict):
    result_dict = {}

    for name, abbs_and_score in names_abbs_dict.items():
        min_score = min(abbs_and_score.values())
        min_abbs = [abb for abb, score in abbs_and_score.items() if score == min_score]
        result_dict[name] = {min_abb: min_score for min_abb in min_abbs}

    return result_dict