n = int(input())
c = {}
alpha = list(range(2005, 2023)) + [2003, 2004]

for i in range(n):
    name = input()
    ch = alpha[ord(name[0].lower()) - 97]
    c[ch] = c.get(ch, 0) + 1
sor = sorted(c.items(), key=lambda x: x[1])

res = []

for key, val in sor:
    res.append(f"{key} {val}")

print('\n'.join(res))
