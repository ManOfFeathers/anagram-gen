import random

def anagram(name):
    s = name    # converts input to string
    b = len(s)  # b for blank spaces
##    r = b - 1   # range of numerical values assigned to characters
    a = []      # array to be filled by rearranged letters
    for i in range (b):
        ##r = random.randint(0,b)
        a.append(i)
    return(a)

print(anagram("thomas"))
