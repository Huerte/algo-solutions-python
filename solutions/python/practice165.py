# Problem: Subarray Sum Equals K
# Source: https://leetcode.com/problems/subarray-sum-equals-k/
# Note: Count earlier running totals that are exactly k below the current total.

# My Solution
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) == k:
                    count += 1
        
        return count

# Accepted Solution
# Each earlier match marks a starting point, so the map stores frequencies.
# The initial zero handles subarrays that start at the first element. Look up
# matches before storing the current total so an empty subarray never counts.
# Expected O(n) time and O(n) extra space.
class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        curSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res

s = Solution()
print(s.subarraySum([1, 1, 1], 2))   # Expected: 2
# print(s.subarraySum([1, 2, 3], 3))   # Expected: 2
