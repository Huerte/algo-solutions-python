# Left and Right Sum Differences

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
