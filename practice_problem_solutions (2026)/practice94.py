# First Matching Character From Both Ends

class Solution(object):
    def firstMatchingIndex(self, s):
        n = len(s)
        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i
        return -1