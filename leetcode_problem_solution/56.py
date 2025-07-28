n = int(input())
c = 0
while n > 1:
    c += 1
    if n % 2 == 0:
        n /= 2
    else:
        if (n-1) / 2 % 2 == 0 or (n-1) / 2 == 1:
            n -= 1
        else:
            n += 1

print(f"Minimum number of operations: {c}")