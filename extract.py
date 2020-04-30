#!/usr/bin/env python3
import utils
import sys
level = 10000
if(len(sys.argv) > 1):
    level = int(sys.argv[1])
utils.extract(level=level)
