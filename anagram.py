##import random

def anagram(name):
    s = name    # converts input to string
    b = len(s)  # b for blank spaces
    a = []      # array to be filled by rearranged letters
##    a2 = []
##    r = random.randint(0,b)
##    
##    for i in range(b):
##        np = a[r]
##        a2.append(np)
    for i in range(b):
        a.append(i)

    return(a)
print(anagram("tartuffe"))
