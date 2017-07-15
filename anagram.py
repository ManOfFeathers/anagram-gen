import random

def char_array(name):
    s = name                # converts input to string
    b = len(s)              # b for blank spaces                        
    a = [c for c in s]      # array to be filled by rearranged letters 
    random.shuffle(a)       # mix up array letters
    return "".join(a)       # generate results as a string

print(char_array("tartuffe"))

# function currently in progress

##def anagram(name):
##    s = name    
##
##    d = s.split("r",2)
##
##    a2 = [c for c in d]
##
##    random.shuffle(a2)
##
##    for t in d:
##        print(t)
##    return "r".join(a2)
##
##print(anagram("tartuffe"))
