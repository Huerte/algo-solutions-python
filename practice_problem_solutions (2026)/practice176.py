# Count Number of Pairs With Absolute Difference K

class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        for i in range(len(nums)  - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
    
s = Solution()
print(s.countKDifference([1,2,2,1], 1))   # 4
print(s.countKDifference([1,3], 3))       # 0
print(s.countKDifference([3,2,1,5,4], 2)) # 3
