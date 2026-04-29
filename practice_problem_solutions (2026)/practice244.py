# Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        counts = []

        i = 0
        while i < len(nums):
            count = 0
            j = i
            while j < len(nums) and nums[j] == 1:
                count += 1
                j += 1
            if count > 0:
                counts.append(count)
                i = j
            i += 1
        
        return max(counts) if counts else 0

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1])) # 2
print(s.findMaxConsecutiveOnes([0,0,0,0,0,0])) # 0
print(s.findMaxConsecutiveOnes([]))            # 0