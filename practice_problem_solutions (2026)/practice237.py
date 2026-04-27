from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums) -> bool:
        num = Counter(nums)
        for n in num.values():
            if n > 2:
                return False
        return True

s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))     # True
print(s.isPossibleToSplit([1,1,2,2,2,2,3,4])) # False