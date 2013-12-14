#!/usr/bin/env python
"""
Problem 28
11 October 2002
 
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same
way?

Answer: ?????
"""

# TODO: Some explanation
def solve():
    square = 1001
    s = 0
    for i in xrange(3,square+1,2):
        n = i**2
        s += n
        s += n - (i-1)
        s += n - 2*(i-1)
        s += n - 3*(i-1)

    return s+1

if __name__ == '__main__':
    print "Answer:", solve()

