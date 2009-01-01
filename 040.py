#!/usr/bin/env python
"""
Problem 40
28 March 2003
 
An irrational decimal fraction is created by concatenating the positive
integers:

        0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

        d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

Answer: ?????
"""

def solve():
    # Brute-force solution
    s = "".join(str(n) for n in xrange(1,1000000))
    return int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * \
           int(s[9999]) * int(s[99999]) * int(s[999999])

if __name__ == '__main__':
    print "Answer: %s" % solve()

