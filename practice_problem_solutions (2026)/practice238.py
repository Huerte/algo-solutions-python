# Difference Between Element Sum and Digit Sum of an Array

class Solution:
    def differenceOfSum(self, nums) -> int:
        return abs(sum(nums) - sum(map(int, ''.join(map(str, nums)))))

s = Solution()
print(s.differenceOfSum([1,15,6,3])) # 9
print(s.differenceOfSum([1,2,3,4]))  # 0