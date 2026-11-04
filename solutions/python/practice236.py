# Sum of Variable Length Subarrays
# Problem: Sum of Variable Length Subarrays
# Source: https://leetcode.com/problems/sum-of-variable-length-subarrays/
# Note: Calculates the sum of subarrays ending at each index using the current element to determine the starting index.
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
