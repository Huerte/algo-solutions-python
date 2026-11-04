# HackerRank - Calendar Module
# Problem: Calendar Module
# Source: https://www.hackerrank.com/challenges/calendar-module/problem
# Note: Converts the given month, day, and year into a date object and determines the weekday using datetime, then prints the day in uppercase.
from datetime import datetime
d = list(map(int, input().split()))
da = datetime(day=d[1], month=d[0], year=d[-1])
print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][da.weekday()])
