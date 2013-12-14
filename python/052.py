#!/usr/bin/env python
"""
Problem 52
12 September 2003
 
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

Answer: ?????
"""

def solve():
    # Need to test for x in the form 1.0Ey -> 1.(6)Ey
    for y in xrange(1,7):
        for x in xrange(10*10**(y-1), 17*10**(y-1)):
            digits = set(str(x))
            if all([digits == set(str(k*x)) for k in xrange(2,7)]):
                return x

if __name__ == '__main__':
    print "Answer: %s" % solve()

