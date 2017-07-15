import random
import urllib.request
from collections import defaultdict

##def char_array(name):
##    s = name                # converts input to string
##    b = len(s)              # b for blank spaces                        
##    a = [c for c in s]      # array to be filled by rearranged letters 
##    random.shuffle(a)       # mix up array letters
##    return "".join(a)       # generate results as a string
##
##print(char_array("jean flaherty"))

# function currently in progress
# function coded with help from https://rosettacode.org/wiki/Anagrams#Python

def anagram(name):
    s = name
    ws = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split() 
                            # ws for words, put each word on its own line
    ana = defaultdict(list)
    gram = None             # an empty anagram-related variable

    for w in ws:
        ana[tuple(sorted(w))].append(w)
        
    for key, l in ana.items():
        l = [y.decode() for y in l]
        if s in l:
            gram = l
    return gram
    
print(anagram("angle"))

def new_anagram(sentence):
    l = sentence.split() # new list
    nl = []
    for w in l:
        ana = anagram(w)
        if ana:
            choice = random.choice(anagram(w))
            nl.append(choice)
        else:
            nl.append(w)
    return " ".join(nl)

print(new_anagram("erasmus tied cartesian silt citrus"))
    
