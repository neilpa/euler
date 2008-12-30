#!/usr/bin/env python
"""
Problem 15
19 April 2002
 
Starting in the top left corner of a 2*2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

TODO: Figure out how to insert these images

How many routes are there through a 20*20 grid?

Answer: ?????
"""

map = {}

def routes(x, y):
    """Calculate unique routes across the diagonal of an an x by y grid"""
    if 1 == x and 1 == y:
        return 2
    elif 0 == x or 0 == y:
        return 1
    elif (x,y) in map:
        return map[(x,y)]
    elif (y,x) in map:
        return map[(y,x)]
    else:
        map[(x,y)] = routes(x-1, y) + routes(x, y-1)
        return map[(x,y)]

def solve():
    #print routes(2,2)
    return routes(20,20)

if __name__ == '__main__':
    print "Answer: %s" % solve()

