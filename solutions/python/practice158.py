# Contains Duplicate
# Problem: Contains Duplicate
# Source: https://leetcode.com/problems/contains-duplicate/
# Note: Checks whether an array contains any duplicate elements using a set.

class Solution:
    def hasDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

s = Solution()
print(s.hasDuplicate([1, 2, 3, 1]))  # Output: True
print(s.hasDuplicate([1, 2, 3, 4]))  # Output: False
