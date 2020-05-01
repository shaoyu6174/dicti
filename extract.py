#!/usr/bin/env python3
import utils
import sys
level = 10000
if(len(sys.argv) > 1):
    level = int(sys.argv[1])
wordlist = utils.extract(level=level)
count = 0
with open("input.txt", 'w') as f:
    for word in wordlist:
        if word.isalpha():
            f.write(word)
            f.write("\n")
            count+=1

print(str(count) + " words extracted at level " + str(level))
