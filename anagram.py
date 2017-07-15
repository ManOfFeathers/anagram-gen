import random
import urllib.request
from collections import defaultdict

def char_array(name):
    s = name                # converts input to string
    b = len(s)              # b for blank spaces                        
    a = [c for c in s]      # array to be filled by rearranged letters 
    random.shuffle(a)       # mix up array letters
    return "".join(a)       # generate results as a string

print(char_array("tartuffe"))

# function currently in progress
# function coded with help from https://rosettacode.org/wiki/Anagrams#Python

def anagram(name):
    s = name
    b = len(s)
    ws = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split() 
    # ws for words, put each word on its own line
    an = defaultdict(list)
    for w in ws:
        an[tuple(sorted(w))].append(w)
    gram = None # an empty anagram-related variable

    for key, l in an.items():
        l = [x.decode() for x in l]
        if name in l:
            gram = l
    return gram
    
print(anagram("gsdfgsre"))
