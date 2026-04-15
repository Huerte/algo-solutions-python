# Number Complement

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