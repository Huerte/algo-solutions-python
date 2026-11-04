# HackerRank - Day of the Programmer
# Problem: Day of the Programmer
# Source: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Note: Determines the 256th day of the year while accounting for Julian, Gregorian, and the 1918 calendar transition.
def dayOfProgrammer(year):
    if year < 1919:
        days = 243 if year % 4 != 0 else 244
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = 244
        else:
            days = 243
    
    if year == 1918:
        days -= 13
