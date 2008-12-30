#!/usr/bin/env python
"""
Problem 56
07 November 2003
 
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?

Answer: ?????
"""

def solve():
    return max([sum([int(c) for c in str(a**b)]) for a in xrange(90,100) for b in xrange(90,100)])

if __name__ == '__main__':
    print "Answer:", solve()

