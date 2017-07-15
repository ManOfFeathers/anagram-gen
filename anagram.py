import random

def char_array(name):
    s = name    # converts input to string
    b = len(s)  # b for blank spaces
    a = []      # array to be filled by rearranged letters 

    for i in range(b):
        a.append(i)
    
    return(a)
print(char_array("tartuffe"))

def anagram(name):
    s = name    
    b = len(s)

    a2 = char_array(s)

    for i in range(b): 
        r = random.randint(0,b)
        a2[i] = r
        if (a2[i-1] == r):
           r = random.randint(0,b)
           a2[i] = r
        a2.append(r)
    return(a2)

print(anagram("tartuffe"))
