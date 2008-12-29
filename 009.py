#!/usr/bin/env python
"""
Problem 9
25 January 2002
 
A Pythagorean triplet is a set of three natural numbers,
    a<b<c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
the product abc.

Answer: ?????
"""

def solve():
    # Start with a=332, b=333, c=335 and work outwards
    for a in xrange(332,0,-1):
        for b,c in zip(xrange(a+1, 1000), xrange(1000-2*a-1,0,-1)):
            if c < b: break
            if a**2 + b**2 == c**2: return a*b*c

if __name__ == '__main__':
    print "Answer:", solve()

