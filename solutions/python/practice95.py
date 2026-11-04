# Problem: Running Sum of 1D Array
# Source: https://leetcode.com/problems/running-sum-of-1d-array/

n = int(input('Enter the number of integers (N): '))
print(f"Enter {n} integers:")
arr = [int(input()) for _ in range(n)]
res = []
for i in range(1, n + 1):
    res.append(sum(arr[:i]))
print(f"Running sums are:")
print(' '.join(map(str, res)))