# Trim Trailing Vowels
# Problem: Trim Trailing Vowels
# Source: https://leetcode.com/problems/trim-trailing-vowels/
# Note: Removes all consecutive vowels from the end of a string while preserving the rest of the string.
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip('aeiou')
    
s = Solution()
print(s.trimTrailingVowels("a"))    # ""
print(s.trimTrailingVowels("ba"))   # "b"
print(s.trimTrailingVowels("idea")) # "id"
