#!/usr/bin/env ruby

# Longest Collatz sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
#       n -> n/2 (n is even)
#       n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#       13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10
# terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz n
    return Enumerator.new do |c|
        while n > 1
            c.yield n
            n = n.even? ? n / 2 : n * 3 + 1
        end
        c.yield 1
    end
end

def p14
    limit = 999999
    terms = Array.new(limit+1, 0)

    for x in 1..limit
        for n in collatz(x)
            if n >= terms.length || terms[n] == 0
                terms[x] += 1
            else
                terms[x] += terms[n]
                break
            end
        end
    end

    return terms.index(terms.max)
end

# This funcitional approach is way slower than the iterative version above
#def p14
#    limit = 1000
#    lengths = Hash[1 => 1]
#
#    (1..limit).each do |n|
#        gen = collatz(n)
#        chain = gen.take_while { |x| !lengths[x] }
#        chain.reverse.reduce(gen.next) do |previous, current|
#            lengths[current] = lengths[previous] + 1
#            current
#        end
#    end
#
#    return lengths.reduce { |(km, vm), (k,v)| vm < v ? [k,v] : [km,vm] }
#end

if __FILE__ == $0
    puts p14
end

