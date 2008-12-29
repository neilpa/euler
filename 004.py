#!/usr/bin/env python
"""
Problem 4
16 November 2001
 
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: ?????
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solve():
    for p in [x for x in xrange(999**2, 0, -1) if is_palindrome(x)]:
        for m in xrange(999,99,-1):
            if 0 == p%m and 3 == len(str(p/m)):
                return p

if __name__ == '__main__':
    print "Answer:", solve()

