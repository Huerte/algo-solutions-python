# Find Majority Element
# Problem: Majority Element
# Source: https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
# Note: Finds the element occurring more than half the size of the array.

arr = list(map(int, input().split()))

from collections import Counter
import sys

half = len(arr) // 2 + 1

for k, val in Counter(arr).items():
    if val >= half:
        print(k)
        sys.exit()

print(-1)
