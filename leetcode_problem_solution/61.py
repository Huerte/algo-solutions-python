from collections import Counter

s = input('Enter a string: ')

c = Counter(sorted(s))

for k, v in c.items():
    if v > 1:
        print(f'{k}{v}', end='')
    else:
        print(k, end='')