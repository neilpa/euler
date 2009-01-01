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

import divisor

def solve():
    # Can be easily solved with pen+paper
    # product of primes * multiples of primes for rest
    # 2*3*5*7*11*13*17*19 * 2*2*2 * 3
    return divisor.LCM(range(1,21))

if __name__ == '__main__':
    print "Answer: ", solve()

