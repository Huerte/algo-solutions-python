# Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        return chr(sum([ord(c) for c in t]) - sum([ord(c) for c in s]))

s = Solution()
print(s.findTheDifference("abcd", "abcde")) # e
print(s.findTheDifference("", "y"))          # y
print(s.findTheDifference("a", "aa"))       # a