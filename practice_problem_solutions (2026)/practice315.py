# Sort Array by Increasing Frequency

from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))



s = Solution()
print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1])) # [5,-1,4,4,-6,-6,1,1,1]
print(s.frequencySort([1,1,2,2,2,3])) # [3,1,1,2,2,2]
print(s.frequencySort([2,3,1,3,2]))   # [1,3,3,2,2]