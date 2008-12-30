#!/usr/bin/env python
"""
Problem 17
17 May 2002
 
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.

Answer: ?????
"""

def num2word(num):
    ones = ('','one','two','three','four','five','six','seven','eight','nine',
            'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
            'seventeen','eighteen','nineteen')

    tens = ('','','twenty','thirty','forty','fifty','sixty',
            'seventy','eighty','ninety')

    h = num / 100 # hundreds
    r = num % 100 # remainder
    t = r / 10  # tens
    o = r % 10  # ones

    word = []

    if h:
        # hundred [and]
        word += [ones[h], 'hundred']
        if r:
            word += ['and']

    if r < len(ones):
        # handle teens
        word += [ones[r]]
    else:
        # tens and ones
        word += [tens[t], ones[o]]

    return "".join(word)

def solve():
    return sum(len(num2word(n)) for n in xrange(1,1000)) + len('onethousand')

if __name__ == '__main__':
    print "Answer: %s" % solve()

