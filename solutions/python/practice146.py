# Left and Right Sum Differences
# Problem: Left and Right Sum Differences
# Source: https://leetcode.com/problems/left-and-right-sum-differences/
# Note: Calculates the absolute difference between the sum of elements to the left and right of each index.

class Solution(object):
    def leftRightDifference(self, nums):
        if len(nums) == 1:
            return [0]
        
        left = [0]
        right = []

        for i in range(len(nums) - 1):
            left.append(sum(nums[:i+1]))
        
        for i in range(1, len(nums)):
            right.append(sum(nums[i:]))
        right.append(0)

        res = []

        for i, j in zip(left, right):
            res.append(abs(i - j))
        
        return res

s = Solution()
print(s.leftRightDifference([10,4,8,3]))
print(s.leftRightDifference([1]))
