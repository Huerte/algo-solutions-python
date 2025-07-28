n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

val = set(num)
current_max = -1
key = None
for x in val:
    if x % 2 != 0:
        continue
    if num.count(x) > current_max:
        current_max = num.count(x)
        key = x
    elif num.count(x) == current_max and x < key:
        key = x
print(key)