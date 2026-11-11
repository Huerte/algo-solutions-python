# Permutation Difference between Two Strings
# Problem: Permutation Difference between Two Strings
# Source: https://leetcode.com/problems/permutation-difference-between-two-strings/
# Note: Calculates the sum of absolute position differences of matching characters in two strings.

class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            res += abs(i - t.index(s[i]))
        return res
