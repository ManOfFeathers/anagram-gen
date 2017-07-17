import random
import urllib.request
from collections import defaultdict

def char_array(name):
    s = name                # converts input to string
    b = len(s)              # b for blank spaces                        
    a = [c for c in s]      # array to be filled by rearranged letters 
    random.shuffle(a)       # mix up array letters
    return "".join(a)       # generate results as a string

# function currently in progress
# function coded with help from https://rosettacode.org/wiki/Anagrams#Python

def anagram(name):
    s = name
    ws = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
                            # https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
                            # http://www.puzzlers.org/pub/wordlists/unixdict.txt
                            # http://www-01.sil.org/linguistics/wordlists/english/
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

def new_anagram(sentence):
    l = sentence.split() # new list
    nl = []
    for w in l:
        ana = anagram(w) # calls function that scrambles one word
        if ana:
            choice = random.choice(anagram(w))
            nl.append(choice)
        else:
            nl.append(w)
    return " ".join(nl)

print(new_anagram("erasmus tied cartesian silt citrus")) # used for testing

def best_anagram(string):
    l = string.split()
    nl = []
    for w in l:
        ana = anagram(w)
        g = char_array(string) # g for gibberish
        nl.append(g)
        if ana:
            choice = random.choice(anagram(w))
            nl.append(choice)
        else:
            nl.append(w)
##    return " ".join(nl)
    return(nl)

print(best_anagram("erasmus tied cartesian silt citrus")) # used for testing

# erasmus tied cartesian silt citrus
