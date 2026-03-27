# Check If All A's Appears Before All B's

s = input('Enter the string: ')

a_index = []
b_index = []

for i in range(len(s)):
    if s[i] == 'a':
        a_index.append(i)
    else:
        b_index.append(i)

res = False
if not a_index or not b_index:
    res = True
elif max(a_index) < min(b_index):
    res = True

print(res)