# Problem: Largest Number At Least Twice of Others
# Source: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Note: Finds the maximum, then checks that every other element is at most half of it; prints the maximum's index if all pass, otherwise -1

n = int(input('Enter the number of integers: '))
print('Enter the integers:')
arr = [int(input()) for _ in range(n)]
great = max(arr)
dominant = -1
count = 0
for num in arr:
    if num == great:
        continue
    
    if num * 2 <= great:
        count += 1
    
if count == (n - 1):
    dominant = arr.index(max(arr))

print(f'Dominant Index: {dominant}')
