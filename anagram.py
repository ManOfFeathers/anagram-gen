#
# Anagram generator
# Programmed by Griffin Myers
# Based on code from https://rosettacode.org/wiki/Anagrams#Python
#
# wl1.txt -- http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
# wl2.txt -- https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
# wl3.txt -- http://www.puzzlers.org/pub/wordlists/unixdict.txt
# wl4.txt -- http://www-personal.umich.edu/~jlawler/wordlist
#

from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import random
# import urllib.request
#
# ws = urllib.request.urlopen('http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt').read().split()

def readtxtfile():
    with open("supplemental/wl3.txt", "r") as file:
        txt = file.read().split()
        print(txt)
        return txt

ws = readtxtfile()
# print(ws)

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
        l = [y for y in l] # l = [y.decode() for y in l]
        if s in l:
            gram = l
    return gram

def scramble_checker(sentence, min_len): # for each word in sentence, anagrams that word
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
    # return "".join(nl)
    return nl

def bestest_anagram(string, min_len):
    nl = [string]
    el = []
    while nl:
        sub_s = best_anagram(string, min_len)
        el.append(sub_s)
        # nl.remove(sub_s)
    return el

# print(char_array("erasmus tied cartesian silt citrus"))
# print(word_tokenize("erasmus tied cartesian silt citrus"))
# print(len(word_tokenize("erasmus tied cartesian silt citrus")))
# print(scramble_checker("erasmus tied cartesian silt citrus", 3))
# print(scramble_checker(char_array("erasmus tied cartesian silt citrus"), 3)) # used for testing

# print(best_anagram("erasmus tied cartesian silt citrus", 3)) # used for testing

print(best_anagram("erasmus tied cartesian silt citrus", 3))

# erasmus tied cartesian silt citrus
