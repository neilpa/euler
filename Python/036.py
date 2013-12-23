#!/usr/bin/env python
"""
Problem 36
31 January 2003
 
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Answer: ?????
"""

try:
    from gmpy import digits
except ImportError:
    def digits(n, base):
        if base == 10:
            return str(n)
        elif base < 10:
            if n == 0: return '0'
            s = ''
            while n > 0:
                s = str(n % base) + s
                n /= base
            return s
        elif base == 16:
            return hex(n)
        else:
            raise "Unsupported base"

def pal(n): 
    return n == n[::-1]

def solve():
    #for n in range(1,1000000):
    #    if pal(str(n)) and pal(digits(n, 2)):
    #        print n

    return sum(n for n in xrange(1,1000000) if pal(str(n)) and pal(digits(n, 2)))

if __name__ == '__main__':
    print "Answer:", solve()

