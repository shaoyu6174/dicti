#!/usr/bin/env python3
import utils
import sys
level = 10000
with open("text.txt", 'r') as f:
    text = f.read()
path = "input.txt"
if len(sys.argv) > 1:
    level = int(sys.argv[1])
if len(sys.argv) > 2:
    path = sys.argv[2]


wordlist = utils.extract(text, level=level)
utils.writelist(wordlist, path)

print(str(len(wordlist)) + " words extracted at level " + str(level))
