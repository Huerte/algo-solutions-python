# Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        return bin(n)[2:].count('1')

s = Solution()
print(s.hammingWeight(11)) # 3
print(s.hammingWeight(128)) # 1
print(s.hammingWeight(4294967293)) # 31