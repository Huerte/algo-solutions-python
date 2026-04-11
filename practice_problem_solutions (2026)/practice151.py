# Sum of Variable Length Subarrays

class Solution(object):
    def subarraySum(self, nums):
        arr = []

        for i in range(len(nums)):
            s = max(0, i - nums[i])
            arr.append(sum(nums[s:i + 1]))

        return sum(arr)

s = Solution()
print(s.subarraySum([2,3,1]))   # 11
print(s.subarraySum([3,1,1,2])) # 13