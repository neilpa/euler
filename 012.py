#!/usr/bin/env python
"""
Problem 12
08 March 2002
 
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

        1:  1
        3:  1,3
        6:  1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?

Answer: ?????
"""
import primes

def prod(terms):
    return reduce(lambda a,b: a*b, terms)

def divisor_count(n):
    return prod(e+1 for p,e in primes.factorize(n))

def triangle():
    i,t = 1,1
    while 1:
        yield t
        i += 1
        t += i

def solve():
    for t in triangle():
        # TODO: Fix primes.factorize for 1
        if t > 1 and divisor_count(t) > 500:
            #p23 = __import__('023')
            #print p23.divisors(t)
            return t

if __name__ == '__main__':
    print "Answer:", solve()
