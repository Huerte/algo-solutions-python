# Sum of Values at Indices With K Set Bits

class Solution:
    def sumIndicesWithKSetBits(self, nums, k) -> int:
        return sum(num for i, num in enumerate(nums) if bin(i)[2:].count('1') == k)

s = Solution()
print(s.sumIndicesWithKSetBits([5,10,1,5,2], 1)) # 13
print(s.sumIndicesWithKSetBits([4,3,2,1], 2))    # 1