#!/bin/python
from collections import Counter
def find_dup_char(inp):
    wc =Counter(inp)
    j = -1
    for i in wc.values():
        j = j + 1
        if(i> 1):
            print(wc.keys()[j],j)

inp="GeeksForGeeks"
find_dup_char(inp)
