# Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):
        
        left = 0
        right = len(nums) - 1

        res = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1

        res.reverse()
        return res
    
# 2nd solution
class Solution(object):
    def sortedSquares(self, nums):
        return sorted(num ** 2 for num in nums)

s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10])) # [0, 1, 9, 16, 100]
print(s.sortedSquares([-7, -3, 2, 3, 11])) # [4, 9, 9, 49, 121]