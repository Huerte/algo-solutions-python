# Remove Trailing Zeros From a String
# Problem: Remove Trailing Zeros From a String
# Source: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
# Note: Removes all consecutive '0' characters from the end of a numeric string while preserving zeros in the middle.
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.strip('0')
    
s = Solution()
print(s.removeTrailingZeros("51230100")) # "512301"
print(s.removeTrailingZeros("123"))      # "123"
