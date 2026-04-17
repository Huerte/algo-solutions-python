# HackerRank - Calendar Module

from datetime import datetime
d = list(map(int, input().split()))
da = datetime(day=d[1], month=d[0], year=d[-1])
print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][da.weekday()])