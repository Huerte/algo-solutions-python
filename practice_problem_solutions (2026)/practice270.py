# GeeksforGeeks - Implement Atoi

class Solution:
    def myAtoi(self, s):
        digits = ""
        for i, c in enumerate(s.strip()):
            if not c.isdigit() and i > 0:
                break
            elif i == 0 and c in ["-", "+"]:
                digits += c
            else:
                digits += c
        
        peak = 2 ** 31 - 1
        deep = -2 ** 31
        n = int(digits)
        if n > peak:
            n = peak
        elif n < deep:
            n = deep
        return n

s = Solution()
print(s.myAtoi("-999999999999")) # -2147483648
print(s.myAtoi("  -0012gfg4"))   # -12
print(s.myAtoi("-123"))          # -123