'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    
    # If the length of the word is 0 or less than 2 characters,
    # count_th should return 0
    if len(word) == 0:
        return 0

    elif len(word) < len('th'):
        return 0
    # /////////////////////////////////////////////////////
    # the next two characters are scanned.
    # if they do not match 'th', the list moves back one space
    # from the second character
    if word[:2] != 'th':
        return count_th(word[1:])
    # in the event that it does, a '1' is returned and
    # the process repeats until count_th iterates through
    # the entire string.
    else:
        return count_th(word[1:]) + 1
    
# Should return 5 in the example below
print(count_th('othothothothotho')) 
    

    


