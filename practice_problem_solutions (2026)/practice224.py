# Not in place

w = "ABCDFEGH"
alp = [chr(i).upper() for i in range(97, 123)]


import sys
prev = None

for i in w:
    if prev and alp.index(i) < prev:
        print(i)
        sys.exit()
    prev = alp.index(i)
 