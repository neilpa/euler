#!/usr/bin/env python
"""
Problem 19
14 June 2002

You are given the following information, but you may prefer to do some research
for yourself.

   * 1 Jan 1900 was a Monday.
   * Thirty days has September,
     April, June and November.
     All the rest have thirty-one,
     Saving February alone,
     Which has twenty-eight, rain or shine.
     And on leap years, twenty-nine.
   * A leap year occurs on any year evenly divisible by 4, 
     but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?

Answer: 171
"""

# January 1, 1901 is Tuesday
days_before_sunday = 5

def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12): return 31
    elif month in (4, 6, 9, 11): return 30
    elif 0 == year % 4: return 29
    else: return 28

def solve():
    days = 0
    sundays = 0
    for y in xrange(1901,2001):
        for m in xrange(1,13):
            if days_before_sunday == days % 7:
                #print "year", y, "month", m
                sundays += 1
            days += days_in_month(y, m)
    return sundays

if __name__ == "__main__":
    print "Answer:", solve()

