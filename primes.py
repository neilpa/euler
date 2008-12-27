#! /usr/bin/env python
"""Methods for working with prime numbers"""

#TODO:
#better naming schemes 
#memory growth pattern
#binary search
#wrapper class for __sieve and __primes
#different algo for larger primes
#couple of unit tests
#change factorize to not use a dict
#throw away sieve when done with it??
#initialization routine

# Start to hit issues once sieve grows beyond several million
__LIMIT = int(3e7)

# Two is our only prime for now
__primes = [2]

# __sieve[i] == i if i is prime, else 0
__sieve = [0, 0, 2]

def __grow(n):
    """Grow the list of primes through n"""
    global  __sieve, __primes

    start = len(__sieve)
    __sieve += range(start, n+1)

    # Eliminate multiples of already known primes
    for p in __primes:
        m = start - start % p # Last multiple of p <= start
        __sieve[m: n+1: p] = [0] * ((n-m)/p + 1)

    # Enumerate remaining numbers looking for primes
    for i in xrange(start, int(n**0.5) + 1):
        if __sieve[i]:
            # Found another prime, eliminate it's multiples
            __sieve[i*i: n+1: i] = [0] * (n/i - i + 1)
    
    # Add the newly found primes to the list
    __primes += [p for p in __sieve[start:] if p] 

def generate(n):
    """Generate list of primes up to n using the Sieve of Eratosthenes"""
    global __sieve, __primes

    # Grow our list of known primes
    if len(__sieve) < n: __grow(n)
    #return [p for p in __primes if p <= n]
    return __primes

def is_prime(n):
    return n in generate(n)

def factorize(n):
    """Find the prime factors of n"""
    # n is prime, therefore it's the only prime factor
    # TODO: is this even necessary?
    if is_prime(n): return [(n, 1)]
    # n isn't prime, find it's factors
    factors = {}
    for i in generate(n):
        # Found all prime factors
        if n == 1: break
        while 0 == n % i:
            if i not in factors: factors[i] = 1
            else: factors[i] += 1
            n /= i
    return factors.items()

def __len__(self):
    return __LIMIT

def __iter__(self):
    class PrimeIter:
        def __init__(self):
            self.idx = 0
        def __iter__(self):
            return self
        def next(self):
            if self.idx < 10:
                self.idx += 1
                return self.idx
            raise StopIteration
    return PrimeIter()

def __contains__(self, item):
    return is_prime(n)

if __name__ == "__main__":
    print "Primes through 5", generate(5)
    print "Prime factors of 12", factorize(12)
    print "Primes through 20", generate(20)
    #print "Lots o' primes", len(generate(__LIMIT))

