import random

def anagram(name):
    s = name    # converts input to string
    b = len(s)  # b for blank spaces
    a = []      # array to be filled by rearranged letters
    a2 = []
    for i in range(b):
        a.append(i)

    r = random.randint(0,b)
    
    for i in range(b):
        np = a[r]
        a2.append(np)

        
    return(a, a2)
print(anagram("tartuffe"))
