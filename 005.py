#!/usr/bin/env python
"""
Problem 5
30 November 2001
 
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?

Answer: ?????
"""

# TODO: move to a common module
def gcd(a,b):
    """Find greatest common divisor with Euclid's Algorithm"""
    while b: a, b = b, a % b
    return a

def lcm(a,b):
    """Calculate lowest common multiple"""
    return (a*b) / gcd(a,b)

def GCD(terms):
    return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
    return reduce(lambda a,b: lcm(a,b), terms)

def solve():
    # Can be easily solved with pen+paper
    # product of primes * multiples of primes for rest
    # 2*3*5*7*11*13*17*19 * 2*2*2 * 3
    return LCM(range(1,21))

if __name__ == '__main__':
    print "Answer: ", solve()

