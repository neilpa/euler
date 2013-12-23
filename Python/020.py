#!/usr/bin/env python
"""
Problem 20
21 June 2002
 
n! means n * (n- 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!

Answer: ?????
"""

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

def solve():
    return sum(int(c) for c in str(factorial(100)))

if __name__ == '__main__':
    print "Answer:", solve()

