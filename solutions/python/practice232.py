# Number of 1 Bits
# Problem: Number of 1 Bits
# Source: https://leetcode.com/problems/number-of-1-bits/
# Note: Converts an integer into its binary representation and counts the number of set bits (1s).
class Solution(object):
    def hammingWeight(self, n):
        return bin(n)[2:].count('1')

s = Solution()
print(s.hammingWeight(11)) # 3
print(s.hammingWeight(128)) # 1
print(s.hammingWeight(4294967293)) # 31
