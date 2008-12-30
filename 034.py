#!/usr/bin/env python
"""
Problem 34
03 January 2003
 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Answer: ?????
"""

# TODO: factorial, sum/prod of digits module
def fac(n):
    if n == 1 or n == 0: return 1
    return n * fac(n-1)

def solve():
    # Precompute factorials
    factorials = dict((str(n),fac(n)) for n in range(10))

    #for n in range(3, 7 * factorials['9']):
    #    if sum(factorials[c] for c in str(n)) == n:
    #        print n

    return sum(n for n in range(3, 7 * factorials['9']) if sum(factorials[c] for c in str(n)) == n)

if __name__ == '__main__':
    print "Answer:", solve()

