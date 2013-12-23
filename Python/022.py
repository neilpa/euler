#!/usr/bin/env python
"""
Problem 22
19 July 2002
 
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Answer: ?????
"""

from __future__ import with_statement

def score(name):
    return sum(ord(c)-ord('A')+1 for c in name)

def solve():
    with open("names.txt") as f:
        names = [name.replace('"','') for name in sorted(f.read().split(","))]
    return sum(score(n)*i for n,i in zip(names, range(1,len(names)+1)))

if __name__ == '__main__':
    print "Answer:", solve()

