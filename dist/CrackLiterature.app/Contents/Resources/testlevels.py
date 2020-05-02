#!/usr/bin/env python3
import utils

wordlist_prev = utils.extract(level=6000)
for level in range(7000, 21000, 1000):
    omitted_words = []
    count = 0
    wordlist_curr = utils.extract(level=level)
    for word in wordlist_prev:
        if word not in wordlist_curr:
            omitted_words.append(word)
    wordlist_prev = wordlist_curr
    if len(omitted_words) > 0:
        print("Level " + str(level) + " omits: " + ", ".join(omitted_words))

print("*"*80)
print("If you see any word you do not understand in the omitted list of any Level, choose the previous level.")
