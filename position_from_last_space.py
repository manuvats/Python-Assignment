'''Importing necessary libraries'''

'''This function is useful in case a name has multiple words
The letter position will be counted from the last space encountered
So that the letter position is counted from the start of the letter of the word it is in and not the start of the whole name'''
def position_from_last_space(lst, index):
    result = index
    for i in range(index - 1, -1, -1):
        if lst[i] == ' ':
            result = index-i-1

    return result