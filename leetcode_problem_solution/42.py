s = "tmmzuxt"
l = []
for i in range(len(s) - 1):
    t = s[i]
    for j in range(i + 1, len(s)):
        if s[j] in t:
            break
        t += s[j]
    l.append(len(t))

print(max(l))