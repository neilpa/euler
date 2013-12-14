#!/usr/bin/env python
"""
Problem 3
02 November 2001
 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: ?????
"""

import divisor

def solve():
    return divisor.prime_factors(600851475143, 50000)[-1][0]

if __name__ == '__main__':
    print "Answer:", solve()

