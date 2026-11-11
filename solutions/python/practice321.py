# Problem: Split the Array
# Source: https://leetcode.com/problems/split-the-array/
# Note: Checks whether an array can be divided into two equal-sized arrays, each containing distinct elements.
from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums) -> bool:
        num = Counter(nums)
        for n in num.values():
            if n > 2:
                return False
        return True

s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))     # True
print(s.isPossibleToSplit([1,1,2,2,2,2,3,4])) # False
