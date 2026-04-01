# Contains Duplicate

class Solution:
    def hasDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

s = Solution()
print(s.hasDuplicate([1, 2, 3, 1]))  # Output: True
print(s.hasDuplicate([1, 2, 3, 4]))  # Output: False