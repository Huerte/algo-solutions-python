# HackerRank - Migratory Birds

from collections import Counter
def migratoryBirds(arr):
    c = Counter(arr)
    return min(arr, key=lambda x: (-c[x], x))

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) # 3
print(migratoryBirds([1, 4, 4, 4, 5, 3]))                # 4
print(migratoryBirds([1, 1, 2, 2, 3]))                   # 1
