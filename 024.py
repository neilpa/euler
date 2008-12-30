#!/usr/bin/env python
"""
Problem 24
16 August 2002
 
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

        012 021 102 120 201 210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

Answer: ?????
"""

#TODO: Both of these should be in a util module
def fac(n): 
    if 1 == n: return 1
    return n * fac(n-1)

def perm(s, n):
    if len(s) == 1:
        return str(s[0])

    p = fac(len(s)-1)

    for i in range(len(s)):
        if p*(i+1) > n:
            return str(s[i]) + perm(s[:i] + s[i+1:], n - i*p)

def solve():
    return perm(range(10), 999999)

if __name__ == '__main__':
    print "Answer:", solve()

