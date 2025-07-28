def percentageString(s, c):
    s.count(c)
    return int((s.count(c) / len(s)) * 100)

print(percentageString("hello", "l"))
print(percentageString("aabbcc", "a"))
print(percentageString("testcase", "t"))