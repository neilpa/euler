#! /usr/bin/env python
"""Methods for working with prime numbers"""

#TODO:
#better naming schemes 
#wrapper class for __sieve and __primes
#different algo for larger primes
#couple of unit tests
#throw away sieve when done with it??
#replace primes.generate with an actual generator
#indexable primes
#provide a start for the list functions

from bisect import bisect

# Start to hit issues once sieve grows beyond several million
__LIMIT = int(3e7)

# Two is our only prime for now
__primes = [2]

# __sieve[i] == i if i is prime, else 0
__sieve = [0, 0, 2]

def ensure_primes(f):
    """Ensure __primes is large enough"""
    def _f(n):
        # Grow our list of known primes
        if len(__sieve) <= n: __grow(n)
        return f(n)
    return _f

def __grow(n):
    """Grow the list of primes through n"""
    global  __sieve, __primes

    if n < 200:
        end = n**2
    else:
        end = n*2

    end = min(end, __LIMIT)

    #TODO: Get rid of most +1's?
    start = len(__sieve)
    __sieve += range(start, end+1)

    # Eliminate multiples of already known primes
    for p in __primes:
        m = start - start % p # Last multiple of p <= start
        __sieve[m: end+1: p] = [0] * ((end-m)/p + 1)

    # Enumerate remaining numbers looking for primes
    for i in xrange(start, int(end**0.5) + 1):
        if __sieve[i]:
            # Found another prime, eliminate it's multiples
            __sieve[i*i: end+1: i] = [0] * (end/i - i + 1)
    
    # Add the newly found primes to the list
    __primes += [p for p in __sieve[start:] if p] 

@ensure_primes
def generate(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes"""
    return __primes[:bisect(__primes, n)]

@ensure_primes
def xprimes(n):
    """Generator for prime numbers up to n"""
    i = 0
    while i < len(__primes) and __primes[i] <= n:
        yield __primes[i]
        i += 1

def lazy(n):
    """Lazily generate primes through n"""

    @ensure_primes 
    def _lazy(n):
        pass

    #TODO: figure this out


@ensure_primes
def is_prime(n):
    return n == __primes[bisect(__primes, n) - 1]

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
    #TODO: Some tests
    pass

