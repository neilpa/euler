#!/usr/bin/env ruby

# Counting Sundays
# Problem 19
#
# You are given the following information, but you may prefer to do some research
# for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century
#   unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

Days = [:Sun, :Mon, :Tue, :Wed, :Thu, :Fri, :Sat]
Months = [:Jan, :Feb, :Mar, :Apr, :May, :Jun, :Jul, :Aug, :Sep, :Oct, :Nov, :Dec]

def leap? y
    return y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)
end

def days y, m
    case Months[m]
    when :Feb
        return leap?(y) ? 29 : 28
    when :Apr, :Jun, :Sep, :Nov
        return 30
    else
        return 31
    end
end

def fom
    Enumerator.new do |g|
        y = 1900
        m = Months.index(:Jan)
        d = Days.index(:Mon)

        loop do
            g.yield [y, Months[m], Days[d % Days.length]]

            d += days y, m
            m += 1
            if (m == Months.length)
                y += 1
                m = 0
            end
        end
    end
end

def p19
    fom.lazy.drop_while { |y,m,d| y < 1901 }.take_while { |y,m,d| y < 2001 }.select { |y,m,d| d == :Sun }.count
end

if __FILE__ == $0
    puts p19
end
