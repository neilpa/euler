#!/usr/bin/env python
"""
Problem 14
05 April 2002
 
The following iterative sequence is defined for the set of positive integers:

        n --> n/2 (n is even)
        n --> 3n + 1 (n is odd)
:
Using the rule above and starting with 13, we generate the following sequence:

    13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer: ?????
"""

def collatz(n):
    while n > 1:
        yield n
        n = n % 2 and 3*n+1 or n/2
    yield 1

def solve():
    limit = 1000000
    terms = [0] * limit
    for x in xrange(1,limit):
        for n in collatz(x):
            if n >= len(terms) or terms[n] == 0:
                terms[x] += 1
            else:
                terms[x] += terms[n]
                # TODO: update terms[x] -> terms[n]
                break

    # Surprisingly, tracking max inside the loop isn't any faster
    return terms.index(max(terms))

if __name__ == '__main__':
    print "Answer: %s" % solve()

