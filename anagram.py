from random import *

def anagram(name):
    s = name    # converts input to string
    b = len(s)  # b for blank spaces
##    r = b - 1   # range of numerical values assigned to characters
    a = []      # array to be filled by rearranged letters
##    r = Random()
##    r2 = int(r * 100) // b 
    for i in range (b):
        if i <= b:
            a.append(i)
    

    return(a)

print(anagram("abraham lincoln"))
