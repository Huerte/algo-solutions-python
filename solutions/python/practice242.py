# Count Digit Appearances
# Problem: Count Digit Appearances
# Source: https://leetcode.com/problems/count-digit-appearances/
# Note: Counts the total occurrences of a target digit across the decimal representations of all numbers using string conversion.
class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        for num in map(str, nums):
            count += num.count(str(digit))
        return count

s = Solution()
print(s.countDigitOccurrences([12,54,32,22], 2)) # 4
print(s.countDigitOccurrences([3], 1))           # 0
