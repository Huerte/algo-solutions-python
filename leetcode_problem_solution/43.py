opp = {
    '}' : '{', ')': '(', ']': '['
}

s = []

b = '{[()()]}'

for c in b:
    if c in opp and opp[c] in s:
        s.pop()
    else:
        s.append(c)

print(not s)