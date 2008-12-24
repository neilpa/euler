#! /usr/bin/env python
"""
Problem 42
25 April 2003

The n^th term of the sequence of triangle numbers is given by, t_n = n/2(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word
value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words?

Answer ?????
"""

from __future__ import with_statement

def sum_of_digits(n, base=10):
    """Calculates the sum of digits of n"""
    return sum([int(d) for d in str(n)])

def sum_of_chars(s):
    """Calculates the sum of chars based on alphabetical position"""
    return sum([ord(c) - ord('a') + 1 for c in s.lower()])

with open('words.txt') as f:
    words = f.read().replace('"', '').split(',')

#TODO: Basic framework for generating sequences
triangles = [n*(n+1)/2 for n in xrange(1,20)]

print len([w for w in words if sum_of_chars(w) in triangles])

