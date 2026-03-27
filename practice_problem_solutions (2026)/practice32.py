# First Letter to Appear Twice

s = input('Enter a string: ')

dis = {}
res = None
for c in s:
    if c not in dis:
        dis[c] = 1
    else:
        dis[c] += 1
    
    if dis[c] == 2:
        res = c
        break
print(f"The first letter to appear twice is: {res}")