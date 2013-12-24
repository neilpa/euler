#!/usr/bin/env ruby

# Names scores
# Problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into alphabetical
# order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

require_relative 'names'

def score name
    name.each_char.map { |c| c.ord - ?A.ord + 1 }.reduce(:+)
end

def p22
    return getNames.sort.each_with_index.map { |n,i| (i+1) * score(n) }.reduce(:+)
end

if __FILE__ == $0
    puts p22
end
