# Problem: Running Sum of 1d Array
# Source: https://leetcode.com/problems/running-sum-of-1d-array/
# Note: Sum each prefix slice to build the running sums.

class Solution(object):
    def runningSum(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            print(nums[:i])
            res.append(sum(nums[:i]))
        return res
    
s = Solution()
print(s.runningSum([1, 2, 3, 4])) # [1,3,6,10]
