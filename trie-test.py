import urllib.request
from collections import defaultdict

words = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
anagram = defaultdict(list) # map sorted chars to anagrams

for word in words:
    anagram[tuple(sorted(word))].append( word )
 
 
count = max(len(ana) for ana in anagram.values())
for key, ana in anagram.items():
    if len(ana) > 1:
        print ([x.decode() for x in ana])

#anagram[tuple(sorted(word))].append( word )
