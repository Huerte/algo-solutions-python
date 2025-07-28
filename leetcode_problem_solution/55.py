# Count Numbers with Unique Digits

n = int(input())
m = pow(10, n)
c = 0
for i in range(m):
    is_unique = True
    arr = []
    while i > 0:
        cur = i % 10
        if cur in arr:
            is_unique = False
            break
        arr.append(cur)
        i //= 10
    if is_unique:
        c += 1

print(f"Count of numbers with unique digits from 0 - {m-1}: {c}")