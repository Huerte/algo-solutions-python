# Geeksforgeeks - Longest Subarray with Sum K

# My Sol;
class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        if sum(arr) == k:
            return n
        
        maxN = 0

        for i in range(n):
            right = n - 1
            while right >= i:
                temp = arr[i:right+1]
                if sum(temp) == k:
                    maxN = max(maxN, len(temp))
                    break
                right -= 1
        
        return maxN
    
# Optimized one
class Solution:
    def longestSubarray(self, arr, k):
        prefix_map = {}
        curr_sum = 0
        max_len = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            
            if curr_sum == k:
                max_len = i + 1
            
            rem = curr_sum - k
            if rem in prefix_map:
                max_len = max(max_len, i - prefix_map[rem])
            
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i
                
        return max_len
    

s = Solution()
print(s.longestSubarray([10, 5, 2, 7, 1, -10], 15))  # 6
print(s.longestSubarray([-5, 8, -14, 2, 4, 12], -5)) # 5
print(s.longestSubarray([1,2,3,4,5], 15))            # 5