# Create Target Array in the Given Order
# Problem: Create Target Array in the Given Order
# Source: https://leetcode.com/problems/create-target-array-in-the-given-order/
# Note: Creates a target array by inserting each number at its corresponding index in the given order.
class Solution(object):
    def createTargetArray(self, nums, index):
        target = []
        for i, num in zip(index, nums):
            target.insert(i, num)
        return target

s = Solution()
print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))  # [0,4,1,3,2]
print(s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))  # [0,1,2,3,4]
print(s.createTargetArray([1], [0]))  # [1]
