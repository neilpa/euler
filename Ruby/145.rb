#!/usr/bin/env ruby

# How many reversible numbers are there below one-billion?
# Problem 145
#
# Some positive integers n have the property that the sum [ n + reverse(n) ] consists
# entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313.
# We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading
# zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?

# TODO This is reasonable for 1e6 but starts to break down after that
#def p145
#    re = /[0,2,4,6,8]/
#    (11..1e9)
#        .reject { |n| n % 2 == 0 } # iterate odds
#        .map { |n| [n, "#{n}".reverse.to_i] } # reverse the num
#        .reject { |n,r| r % 2 == 1 } # max digit must be even
#        .map { |n,r| [n,r,n+r] } # figure out the sum
#        .reject { |n,r,s| re === "#{s}"} # all digits odd?
#        .length
#end

def p145
    while 
end

if __FILE__ == $0
    puts p145 * 2
end
