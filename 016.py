#!/usr/bin/env python
"""
Problem 16
03 May 2002
 
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer: ?????
"""

def solve():
    return sum(int(d) for d in str(2**1000))

if __name__ == '__main__':
    print "Answer:", solve()

