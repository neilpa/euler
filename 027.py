#!/usr/bin/env python
"""
Problem 27
27 September 2002
 
Euler published the remarkable quadratic formula:

        n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula n^2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

        n^2 + an + b, where |a| < 1000 and |b| < 1000
        where |n| is the modulus/absolute value of n
        e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

Answer: ?????
"""

import primes

def seq(a, b):
    n = 0
    while primes.is_prime(n*n + a*n + b):
        n += 1
    return n

def quad_primes(limit):
    res = []
    for a in xrange(-limit+1,limit):
        for b in [1] + primes.generate(limit):
            res.append((seq(a,b), (a, b), a*b))
            res.append((seq(a,-b), (a, -b), a*b))
    return max(res)

def solve():
    return quad_primes(1000)[-1]

if __name__ == '__main__':
    print "Answer: %s" % solve()

