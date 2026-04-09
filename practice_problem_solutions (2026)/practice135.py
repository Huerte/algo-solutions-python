# CodeWars - Highest Rank Number in an Array

from collections import Counter
def highest_rank(arr):
    return max(set(arr), key=lambda x: (Counter(arr)[x], x))

print(highest_rank([1, 2, 3, 2, 1, 3, 3])) # 3
print(highest_rank([1, 1, 2, 2, 3])) # 2
print(highest_rank([1, 2, 3, 4, 5])) # 5