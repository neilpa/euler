#!/usr/bin/env ruby

# Amicable numbers
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def proper_divisors n
    if (n < 2)
        return []
    end

    r = Math.sqrt(n)
    p = (r - 1).ceil
    d = (2..p).collect { |x| [x, n/x] if n % x == 0 }.compact.flatten
    if (r == r.floor)
        d.concat([r.floor])
    end
    return d.concat([1])
end


def p21
    sod = (0..10000).collect { |x| proper_divisors(x).reduce(0, :+) }
    amicable = sod.each_with_index.select { |x, i| x != i && sod[x] == i }

    # Each pair is in the list twice
    return amicable.flatten.reduce(:+) / 2
end

if __FILE__ == $0
    puts p21
end
