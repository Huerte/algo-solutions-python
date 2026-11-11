# Number Complement
# Problem: Number Complement
# Source: https://leetcode.com/problems/number-complement/
# Note: Converts the number to binary, flips each bit (0 to 1 and 1 to 0), and converts the resulting binary string back to an integer.
class Solution(object):
    def findComplement(self, num):
        bina = list(bin(num)[2:])
        for i, c in enumerate(bina):
            bina[i] = '1' if c == '0' else '0'
        return int(''.join(bina), 2)

s = Solution()
print(s.findComplement(5))  # 2
print(s.findComplement(1))  # 0
print(s.findComplement(12)) # 3
