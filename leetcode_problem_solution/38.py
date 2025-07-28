# First letter to apper twice

seen = []
for l in input():
    if l in seen:
        print(l)
        break
    seen.append(l)
