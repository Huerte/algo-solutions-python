# How Many Numbers Are Smaller Than the Current Number
# Problem: How Many Numbers Are Smaller Than the Current Number
# Source: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Note: Counts how many elements in the array are strictly smaller than each element.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    res[i] += 1
        return res

s = Solution()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3])) # [4, 0, 1, 1, 3]
