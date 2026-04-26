# Trim Trailing Vowels

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip('aeiou')
    
s = Solution()
print(s.trimTrailingVowels("a"))    # ""
print(s.trimTrailingVowels("ba"))   # "b"
print(s.trimTrailingVowels("idea")) # "id"