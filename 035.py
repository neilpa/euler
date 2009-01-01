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

import primes

# TODO: Move to the primes module
def circular(n):
    """Determine if n is a circular prime"""
    #if not primes.is_prime(n):
    #    return False

    digits = [d for d in str(n)]

    # Skip any numbers with even digits
    if '2' in digits or '4' in digits or '5' in digits or '6' in digits or '8' in digits:
        if n == 2 or n == 5: return True
        else: return False

    rot = digits[1:] + [digits[0]]
    while rot != digits:
        if not primes.is_prime(int("".join(rot))):
            return False
        rot = rot[1:] + [rot[0]]

    return True

def gen_circular_primes(limit):
    return [p for p in primes.xprimes(limit) if circular(p)]

def solve():
    return len(gen_circular_primes(1000000))

if __name__ == '__main__':
    print "Answer: %s" % solve()

