#!/usr/bin/env python
"""
Problem 67
09 April 2004
 
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

        3
        7 5
        2 4 6
        8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save
Link/Target As...'), a 15K text file containing a triangle with one-hundred
rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 2^99 altogether! If you
could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)

Answer: 7273
"""

from __future__ import with_statement

#TODO: merge with problem 18, i.e. best path

def solve():
    with open("triangle.txt") as f:
        triangle = [[int(n) for n in line.split()] for line in f]

    prev = triangle[-1]
    for row in triangle[-2::-1]:
        for i in xrange(len(row)):
            row[i] += max(prev[i], prev[i+1])
        prev = row

    return triangle[0][0]

if __name__ == '__main__':
    print "Answer:", solve()

