#! /usr/bin/env python
"""
Problem 23
02 August 2002

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number whose proper divisors are less than the number is called deficient and
a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Answer: ?????
"""

# 2: 1
# 4: 1 2
# 8: 1 2 4
# 16: 1 2 4 8

# 3: 1
# 6: 1 2 3
# 12: 1 2 3 4 6
# 24: 1 2 3 4 6 8 12


def divisors(n):
    """Returns a list of all proper divisors of n (i.e. all but n)"""
    return [d for d in xrange(1, n/2+1) if 0 == n % d]

def is_perfect(n):
    return sum(divisors(n)) == n

def is_abundant(n):
    return sum(divisors(n)) > n

def is_defecient(n):
    return sum(divisors(n)) > n

#Generate list of abundant numbers
# FIXME: this is very sloooooow
abundant = [n for n in xrange(1,28124) if is_abundant(n)]
print abundant

inverse = set([a+b for a,b in zip(abundant,abundant) if a+b < 28124])
print inverse
print 
print res = set(range(1,28124)).difference(inverse)
print 
print
print "Answer", len(res)

