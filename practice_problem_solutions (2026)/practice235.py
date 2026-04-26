# Remove Trailing Zeros From a String

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.strip('0')
    
s = Solution()
print(s.removeTrailingZeros("51230100")) # "512301"
print(s.removeTrailingZeros("123"))      # "123"