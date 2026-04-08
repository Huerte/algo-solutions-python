# HackerRank - Compress the String!

s = input()

res = []
i = 0
while i < len(s):
    count = 0
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    i += 1
    res.append((count + 1, int(s[i - 1])))
print(' '.join(map(str, res)))