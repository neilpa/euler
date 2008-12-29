#!/usr/bin/env python
"""
Problem 10
08 February 2002
 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: ?????
"""

import primes

def solve(): 
    return sum(primes.xprimes(2000000))

if __name__ == '__main__':
    print "Answer:", solve()

