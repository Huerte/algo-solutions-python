# Final Array State After K Multiplication Operations I

class Solution(object):
    def getFinalState(self, nums, k, multiplier):

        for _ in range(k):
            cur_min = min(nums)
            for i in range(len(nums)):
                if nums[i] == cur_min:
                    nums[i] *= multiplier
                    break
        
        return nums

s = Solution()
print(s.getFinalState([1, 2, 3], 3, 10)) # [100, 20, 30]
print(s.getFinalState([1, 1, 1], 3, 10)) # [1000, 1, 1]
print(s.getFinalState([1, 2, 3], 0, 10)) # [1, 2, 3]