# Difference Between Element Sum and Digit Sum of an Array
# Problem: Difference Between Element Sum and Digit Sum of an Array
# Source: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Note: Calculates the absolute difference between the sum of array elements and the sum of all their individual digits.
class Solution:
    def differenceOfSum(self, nums) -> int:
        return abs(sum(nums) - sum(map(int, ''.join(map(str, nums)))))

s = Solution()
print(s.differenceOfSum([1,15,6,3])) # 9
print(s.differenceOfSum([1,2,3,4]))  # 0
