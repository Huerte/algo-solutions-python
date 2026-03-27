# Backspace String Compare

s = input('Enter string s: ')
t = input('Enter string t: ')

res = []
for c in s:
    if not res:
        res.append(c)
    elif c == '#':
        res.pop()
    else:
        res.append(c)

if ''.join(res) == t:
    print('true')
else:
    print('false')