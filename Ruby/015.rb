#!/usr/bin/env ruby

# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
#       <lattice.gif>
#
# How many such routes are there through a 20×20 grid?


Memo = Hash.new

def routes x, y
    if x == 0 || y == 0
        return 1
    elsif x == 1 && y == 1
        return 2
    elsif Memo[[x,y]]
        return Memo[[x,y]]
    else
        Memo[[y,x]] = Memo[[x,y]] = routes(x-1, y) + routes(x, y-1)
        return Memo[[x,y]]
    end
end

def p15
    return routes(20,20)
end


if __FILE__ == $0
    puts p15
end

