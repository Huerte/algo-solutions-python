# Sort Colors
# Problem: Sort Colors
# Source: https://leetcode.com/problems/sort-colors/
# Note: Sorts an array containing only 0s, 1s, and 2s in-place without using the built-in sorting function.
class Solution:
    def sortColors(self, nums) -> None:
        nums.sort()
        return nums
