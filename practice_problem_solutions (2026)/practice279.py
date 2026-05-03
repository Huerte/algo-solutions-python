# Combinations

from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        return [list(arr) for arr in combinations(range(1, n + 1), k)]

s = Solution()
print(s.combine(4, 2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(s.combine(4, 3)) # [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
print(s.combine(4, 1)) # [[1], [2], [3], [4]]
print(s.combine(1, 1)) # [[1]]