# Problem: Maximum Subarray
# Source: https://leetcode.com/problems/maximum-subarray/
# Note: Use Kadane's algorithm to track the best sum ending at each element
# Time: O(n), Space: O(n) because nums[1:] creates a copy
# Topic: arrays, dp
# Description:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# A subarray is a contiguous part of an array.
#
# Input:
# - nums: An integer array where 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# Output:
# - An integer representing the maximum subarray sum
#
# Status: ✅ SOLVED

def maxSubArray(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases with assertions
# Example 1
assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

# Example 2
assert maxSubArray([1]) == 1

# Example 3
assert maxSubArray([5,4,-1,7,8]) == 23

# Edge cases
assert maxSubArray([-1]) == -1
assert maxSubArray([-2, -1]) == -1
assert maxSubArray([1, 2, 3, 4]) == 10
assert maxSubArray([-1, -2, -3, -4]) == -1

# All-zero input
assert maxSubArray([0, 0, 0]) == 0

# Zero is better than any negative element
assert maxSubArray([-3, 0, -2]) == 0

# Positive elements separated by a loss cannot be combined arbitrarily
assert maxSubArray([5, -10, 6]) == 6

# The best subarray ends before a large trailing loss
assert maxSubArray([4, -1, 2, -10]) == 5

# Maximum allowed length and element value
assert maxSubArray([10_000] * 100_000) == 1_000_000_000

print("All test cases passed!")
