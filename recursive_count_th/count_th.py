'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = 'th'
def count_th(word):
    

    if word == '':
        return 0

    elif word == 'th' :
        return 1 + count_th(word[1:])
    # print (word.count("th"))
    # # TBC
    
    
    # return word

    
    

    
print(count_th(word))
# count_th("thothothoth")

