#! /usr/bin/env python

# TODO: computation time for solutions

def solve(num):
    """Solves an individual problem"""
    try:
        problem = __import__("%03d" % num)
        answer = problem.solve()
        if answer is None:
            print "Problem %d not solved yet" % num
        else:
            print "Answer to problem %d: %s" % (num, answer)

    except ImportError:
        print "Problem %d doesn't exist yet" % num
    except AttributeError:
        print "Problem %d doesn't follow solution protocol" % num


if __name__ == "__main__":
    import sys
    if not [solve(int(arg)) for arg in sys.argv[1:]]:
        print "Need some problems to solve"

