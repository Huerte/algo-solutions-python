# Smallest Range I

class Solution(object):
    def smallestRangeI(self, nums, k):
        maxt = max(nums) - k
        mint = min(nums) + k
        diff = maxt - mint
        return diff if diff > 0 else 0

s = Solution()
print(s.smallestRangeI([1], 0)) # 0
print(s.smallestRangeI([0, 10], 2)) # 6
print(s.smallestRangeI([1, 3, 6], 3)) # 0