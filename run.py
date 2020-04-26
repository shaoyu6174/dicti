import crawl
import processing
import os
os.remove("result.json") 
with open("input.txt", 'r') as f:
    contents = f.readlines()
    modified = []
    for line in contents:
        modified.append(line.rstrip())
    src = ",".join(modified)

crawl.lookup(src)
processing.do()
