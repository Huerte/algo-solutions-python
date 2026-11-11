# Problem: Rank Transform of an Array
# Source: https://leetcode.com/problems/rank-transform-of-an-array/
# Note: Replace each element with its 1-based rank among the array's distinct sorted values
#
# What this does (in plain English):
# Every number in the array is replaced by its "rank": 1 for the smallest
# distinct value, 2 for the next smallest, and so on. Equal values share the
# same rank, and because ranks are numbered over the UNIQUE values only, they
# are consecutive with no gaps (they always run 1..number-of-distinct-values).
#
# How it works, step by step:
#   1. set(arr) keeps each distinct value once, and sorted() lines them up in
#      ascending order. Example: [40, 10, 20, 30] -> [10, 20, 30, 40].
#   2. range(1, len(set(arr)) + 1) produces the ranks 1, 2, 3, ... and zip()
#      pairs each sorted value with its rank; dict() stores the pairs as a
#      lookup table: {10: 1, 20: 2, 30: 3, 40: 4}.
#   3. The list comprehension walks the ORIGINAL array and replaces each
#      element with its rank from the table, so duplicates keep their shared
#      rank and the original order is preserved.
#
# Walkthrough: [40, 10, 20, 30] -> lookup {10: 1, 20: 2, 30: 3, 40: 4}
#              -> result [4, 1, 2, 3]. And [100, 100, 100] -> [1, 1, 1].
#
# Time complexity:  O(n log n) — sorting the distinct values dominates;
#                   building the table is O(n) and each lookup is O(1) on average.
# Space complexity: O(n) — for the distinct-value set, the rank table, and the result list.

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = dict(zip(sorted(set(arr)), range(1, len(set(arr))+1)))
        return [rank[x] for x in arr]

s = Solution()
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]
print(s.arrayRankTransform([40,10,20,30]))               # [4,1,2,3]
print(s.arrayRankTransform([100,100,100]))               # [1,1,1]