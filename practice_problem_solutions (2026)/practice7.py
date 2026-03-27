# Count Valid Pairs with Equal Values and Divisible Product of Indices

n = int(input('Enter the number of integers (N): '))
print(f'Enter {n} integers:')

res = 0

nums = []

for _ in range(n):
    nums.append(int(input()))

k = int(input('Enter the integer K: '))

for i in range(n - 1):
    for j in range(i + 1, n):
        if (i * j) % k == 0 and (nums[i] == nums[j]):
            res += 1

print(f'Number of valid pairs: {res}')