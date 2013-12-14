#!/usr/bin/env python
"""
Problem 7
28 December 2001
 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

Answer: ?????
"""

import primes

def solve():
    # Prime Number Theorem:
    # Roughly speaking, the prime number theorem states that if you randomly 
    # select a number nearby some large number N, the chance of it being prime 
    # is about 1 / ln(N), where ln(N) denotes the natural logarithm of N. For 
    # example, near N = 10,000, about one in nine numbers is prime, whereas 
    # near N = 1,000,000,000, only one in every 21 numbers is prime.
    return primes.generate(10000)[1001]

if __name__ == '__main__':
    print "Answer:", solve()

