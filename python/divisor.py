#!/usr/bin/env python
"""Methods related to the divisors of numbers"""

import primes

def sod(n):
    """Calculate sum of divisors of n"""
    prod = 1

    for k in primes.xprimes(int(n**0.5)+1):
        p = 1
        while n % k == 0:
            p = p*k+1
            n /= k
        prod *= p

    # n has a prime divisor > sqrt(n)
    if n > 1:
        prod *= 1+n

    return prod;

def sod_proper(n):
    """Calculate sum of proper divisors of n"""
    return divisor.sod(n) - n

def divisors(n):
    """Return a list of all divisors of n"""

    def recurse(d, factors):
        """Compute the products of all combinations of prime factors"""
        if not factors: return [d]
        div = []
        p,e = factors[0]
        while e >= 0:
            div += recurse(d * p ** e, factors[1:])
            e -= 1
        return div

    return recurse(1, prime_factors(n))

def proper(n):
    """Return a list of proper divisors of n (e.g. all divisors but n)"""
    return divisors[:-1]

#TODO:
# Get rid of hint when I have primes.lazy() working
# Fix for n <= 1
def prime_factors(n, hint=None):
    """Return the prime factorization of in the form [(p,e), ...]"""
    if not hint: hint = int(n ** 0.5) + 1

    factors = []
    for p in primes.xprimes(hint):
        # Found all prime factors
        if n <= 1: break

        while 0 == n % p:
            if not factors or factors[-1][0] != p:
                factors.append([p,1])
            else:
                factors[-1][-1] += 1
            n /= p

    if n > 1:
        #print "Hint was too small, %s likely prime" % n
        if n < int(n ** 0.5) + 1:
            factors += prime_factors(n, int(n ** 0.5) + 1)
        else:
            factors += prime_factors(n, n)

    return factors

def count(n):
    """Return the number of divisors of n"""
    def prod(terms):
        return reduce(lambda a,b: a*b, terms)
    if n == 1: return 1
    return prod(e+1 for p,e in prime_factors(n))

def gcd(a,b):
    """Find greatest common divisor with Euclid's Algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    """Calculate lowest common multiple"""
    return (a*b) / gcd(a,b)

def GCD(terms):
    return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
    return reduce(lambda a,b: lcm(a,b), terms)

def is_perfect(n):
    """Is n a perfect number?"""
    return sod(n) == 2*n and n > 0

def is_abundant(n):
    """Is n an abundant number?"""
    return sod(n) > 2*n and n > 0

def is_defecient(n):
    """Is n a defecient number?"""
    return sod(n) < 2*n and n > 0

if __name__ == "__main__":
    #TODO: Some tests
    prime_factors(3)
    pass

