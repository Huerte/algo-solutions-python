# Permutation Difference between Two Strings

class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            res += abs(i - t.index(s[i]))
        return res