# Array Partition

class Solution(object):
    def arrayPairSum(self, nums):
        return sum(num for i, num in enumerate(sorted(nums)) if i % 2 == 0)

s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))       # 4
print(s.arrayPairSum([6, 2, 6, 5, 1, 2])) # 9