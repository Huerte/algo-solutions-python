# HackerRank - Write a function
# Problem: Write a function (Leap Year)
# Source: https://www.hackerrank.com/challenges/write-a-function/problem
# Note: Checks whether a year is a leap year using divisibility rules for 4, 100, and 400.
def is_leap(year):
    leap = False
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400  == 0):
        leap = True
    
    return leap
