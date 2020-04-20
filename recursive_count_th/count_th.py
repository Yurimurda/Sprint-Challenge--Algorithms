'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(char, word):
    if len(word)== 0:
        return 0
    count = 1 if word[0] == char else 0
    return count + count_th(char, word[1:]) 
    # print (word.count("th"))
    # # TBC
    
    pass
    # return word

    
    

    
print (count_th('th', 'thoth'))
# count_th("thothothoth")

