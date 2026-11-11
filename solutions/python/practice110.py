# Problem: Intersection of Two Arrays
# Source: https://leetcode.com/problems/intersection-of-two-arrays/

n = int(input('Enter the size of the first array: '))
print(f"Enter {n} elements of the first array (sorted):")
arr1 = list(map(int, input().split()))

n2 = int(input('Enter the size of the second array: '))
print(f"Enter {n2} elements of the second array (sorted):")
arr2 = list(map(int, input().split()))

res = set(arr1) & set(arr2)

print(f"Unique common elements are: {' '.join(map(str, list(res)))}")