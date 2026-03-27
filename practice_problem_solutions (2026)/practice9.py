# Minimum Operations to Make Integers Divisible by 3

n = int(input('Enter the number of integers (N): '))
print(f'Enter {n} integers:')
arr = [int(input()) for _ in range(n)]

res = 0

for num in arr:
    pos, neg = 0, 0
    temp = num
    while temp % 3 != 0:
        temp += 1
        pos += 1
    while num % 3 != 0:
        num -= 1
        neg += 1
    
    res += min(pos, neg)


print(f'Minimum number of operation: {res}')