#!/usr/bin/env python
"""
Problem 32
06 December 2002
 
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigitial.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Answer: ?????
"""

def rdig(d):
    return range(10**(d-1), 10**d)

def pandigital(a,b,c):
    return "".join(sorted(str(a) + str(b) + str(c))) == "123456789"

#TODO: Some more explanation
def solve():
    digits = ((1,4,4), (2,3,4))
    results = set()

    for a,b,c in digits:
        for i in rdig(a):
            for j in rdig(b):
                if pandigital(i,j,i*j):
                    #print i, "*", j, "=", i*j
                    results.add(i*j)

    #print results, "sum:", sum(results)
    return sum(results)

if __name__ == '__main__':
    print "Answer:", solve()

