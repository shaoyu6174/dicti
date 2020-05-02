#!/usr/bin/env python3
import utils
import sys
level = 10000
path = "input.txt"
if(len(sys.argv) > 1):
    level = int(sys.argv[1])
if(len(sys.argv) > 2):
    path = sys.argv[2]

wordlist = utils.extract(level=level)
count = 0
with open(path, 'w') as f:
    for word in wordlist:
            f.write(word)
            f.write("\n")

print(str(count) + " words extracted at level " + str(level))
