# Problem: Product of Array Except Self
# Source: https://leetcode.com/problems/product-of-array-except-self/

n = int(input('Enter the number of elements: '))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
res = [1] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        res[i] *= arr[j]

print("Product array is:")
print(" ".join(map(str, res)))