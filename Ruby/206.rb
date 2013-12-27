#!/usr/bin/env ruby

# Concealed Square
# Problem 206
#
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

def round_up num, fact
    return num + (fact - num % fact)
end

# TODO - This could probably completed with pen+paper only
def p206
    re = /1.2.3.4.5.6.7.8.9.0/
    max = Math.sqrt(1929394959697989990).floor

    # Round since only squares of multiples of 30 and 70 end with 9_0 (e.g. 900)
    i = round_up Math.sqrt(1020304050607080900).floor, 100
    while i < max
        p30 = (i+30) ** 2
        p70 = (i+70) ** 2

        if re === "#{p30}"
            return "#{i+30}^2 = #{p30}"
        elsif re === "#{p70}"
            return "#{i+70}^2 = #{p70}"
        end

        i += 100
    end
end

if __FILE__ == $0
    puts p206
end

