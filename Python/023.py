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

from __future__ import with_statement

from divisor import is_abundant

#TODO: This isn't completely correct anymore
def solve():
    # Actual limit rather than analytical (28123) from problem description
    # http://en.wikipedia.org/wiki/Abundant_number
    limit = 20160
    res = range(limit+1)

    # Generate list of abundant numbers
    abundant = [n for n in res if is_abundant(n)]

    # Filter out the sums
    # TODO: Make this faster
    for a in abundant:
        for b in abundant:
            if a+b < len(res):
                res[a+b] = 0
    
    return sum(res)

if __name__ == "__main__":
    print "Answer: ", solve()

