# Problem: Reverse Bits
# Source: https://leetcode.com/problems/reverse-bits/

class Solution(object):
    def reverseBits(self, n):
        """ Reverse bits of a given 32 bits unsigned integer."""
        return int(f"{n:032b}"[::-1], 2)

s = Solution()
print(s.reverseBits(43261596))   # 964176192
print(s.reverseBits(2147483644)) # 1073741822