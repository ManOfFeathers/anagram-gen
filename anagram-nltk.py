#
# Anagram generator
# Programmed by Griffin Myers with help from https://rosettacode.org/wiki/Anagrams#Python
#

from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import random
import urllib.request

ws = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
                            # https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
                            # http://www.puzzlers.org/pub/wordlists/unixdict.txt
                            # http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
                            # http://www-personal.umich.edu/~jlawler/wordlist
                            # ws for words, put each word on its own line

def char_array(name):
    s = name                # converts input to string
    b = len(s)              # b for blank spaces
    a = [c for c in s]      # array to be filled by rearranged letters
    random.shuffle(a)       # mix up array letters
    return "".join(a)       # generate results as a string

def anagram(name):
    s = name
    ana = defaultdict(list)
    gram = None # an empty variable

    for w in ws:
        ana[tuple(sorted(w))].append(w)

    for key, l in ana.items():
        l = [y.decode() for y in l]
        if s in l:
            gram = l
    return gram

def scramble_checker(sentence, min_len):
    gl = word_tokenize(sentence) # gibberish list
    nl = []
    for word in gl:
        ana = anagram(word)
        if ana:
            aw = [] # accepted words
            for word in ana:
                if len(word) > min_len:
                    aw.append(word)
            if aw:
                choice = random.choice(aw)
                nl.append(choice)
    return nl

def best_anagram(string, min_len):
    nl = []
    i = 0
    while not nl: # while new list is empty
        print(i) # testing purposes -- shows us that it's thinking
        g = char_array(string) # g for gibberish
        nl = scramble_checker(g, min_len) # nl.append(scramble_checker(g, min_len))
        i += 1
    return nl, i

print(best_anagram("erasmus tied cartesian silt citrus", 4))
##print(word_tokenize("erasmus tied cartesian silt citrus"))

##def smart_anagram(string, min_len):
##    ol = string.split(" ") #old list
##    nl = []
##    i = 0
##    #print(ol)
##    for word in ol:
##        while not nl: # while new list is empty
##            print(i) # testing purposes -- shows us that it's thinking
##            nl = scramble_checker(char_array(word), min_len)  # nl.append(scramble_checker(g, min_len))
##            #del ol[i]
##            if nl:
##                i += 1
##    return nl, i

##print(best_anagram("erasmus tied cartesian silt citrus", 4)) # used for testing

# print(scramble_checker("erasmus tied cartesian silt citrus", 3))
# print(scramble_checker(char_array("erasmus tied cartesian silt citrus"), 3)) # used for testing

# print((output, iters)) # used for testing

# erasmus tied cartesian silt citrus
