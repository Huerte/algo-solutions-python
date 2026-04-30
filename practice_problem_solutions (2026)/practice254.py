# Maximum Subarray

class Solution:
    def maxSubArray(self, nums) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        
        return max_sub

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([5,4,-1,7,8]))            # 23
print(s.maxSubArray([1]))                     # 1