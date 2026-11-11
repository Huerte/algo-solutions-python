# Count Pairs Whose Sum is Less than Target
# Problem: Count Pairs Whose Sum is Less than Target
# Source: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Note: Counts pairs of elements whose sum is strictly less than the target.

class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
