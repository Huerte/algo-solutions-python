# Find Majority Element

arr = list(map(int, input().split()))

from collections import Counter
import sys

half = len(arr) // 2 + 1

for k, val in Counter(arr).items():
    if val >= half:
        print(k)
        sys.exit()

print(-1)