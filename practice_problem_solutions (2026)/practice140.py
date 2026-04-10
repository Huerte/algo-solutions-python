# 4Sum
# Not accepted Solution

class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for n in range(k + 1, len(nums)):
                        if sum([nums[i], nums[k], nums[j], nums[n]]) == target:
                            res.append([nums[i], nums[k], nums[j], nums[n]])
        
        final = []

        for lst in res:
            if final and lst in final:
                continue
            final.append(lst)

        return final

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(s.fourSum([2, 2, 2, 2, 2], 8)) # [[2, 2, 2, 2]]
print(s.fourSum([0, 0, 0, 0], 0)) # [[0, 0, 0, 0]]