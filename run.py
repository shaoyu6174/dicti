#!/usr/bin/env python3
import utils
import os


if os.path.exists("result.json"):
    os.remove("result.json")
with open("input.txt", 'r') as f:
    contents = f.readlines()
    wordlist = []
    for line in contents:
        wordlist.append(line.rstrip())
    words = ",".join(wordlist)

utils.crawl(words)
output = utils.process()
utils.writelist(output, "output.txt")
