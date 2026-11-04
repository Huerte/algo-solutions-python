# First Matching Character From Both Ends
# Problem: First Matching Character From Both Ends
# Source: https://leetcode.com/problems/first-matching-character-from-both-ends/
# Note: Finds the smallest index where a character matches its mirrored character from the opposite end of the string.
class Solution(object):
    def firstMatchingIndex(self, s):
        n = len(s)
        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i
        return -1
