# Average of Array Excluding Minimum and Maximum

n = int(input('Enter the number of integers (N): '))
print(f'Enter {n} integers:')

arr = []
for _ in range(n):
    arr.append(int(input()))

res = sorted(arr)[1:-1]
print(f'Average: {sum(res) / len(res):.2f}')