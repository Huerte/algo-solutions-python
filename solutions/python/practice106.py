# Problem: Backspace String Compare
# Source: https://leetcode.com/problems/backspace-string-compare/
# Note: Builds the final text of s with a list as a stack ('#' pops the last character), then compares the result against t as entered

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