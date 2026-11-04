# GeeksForGeeks - Kadane's Algorithm
# Problem: Kadane's Algorithm
# Source: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Note: Finds the maximum sum of a contiguous subarray using Kadane's Algorithm by tracking the current sum and maximum sum.
class Solution:
    def maxSubarraySum(self, arr):
        cur_max = float('-inf')
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            cur_max = max(cur_max, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return cur_max
    
s = Solution()
print(s.maxSubarraySum([-3, -2, -6, -1, -7, -4]))
