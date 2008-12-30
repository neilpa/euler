#!/usr/bin/env python
"""
Problem 35
17 January 2003
 
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

Answer: ?????
"""

from math import sqrt

# TODO: Cleanup

def primes(max):
    sieve = range(max+1)
    for i in xrange(2, int(sqrt(max))+1):
        if not sieve[i]: continue
        for j in xrange(i*i, max+1, i):
            sieve[j] = None
    #return [p for p in sieve]
    return sieve

def rot(n):
    s = str(n)
    for i in xrange(len(s)):
        r = s[1:] + s[0]
        #if r == s: break
        yield int(r)

def solve():
    sieve = primes(1000000)
    circ = []

    for p in [n for n in sieve if n]:
        gen = rot(p)
        for r in gen:
            if not sieve[r]:
                sieve[p] = None

        if sieve[p]: circ.append(p)

    #print circ[::-1]
    #print len(circ)
    return len(circ)

if __name__ == '__main__':
    print "Answer:", solve()

