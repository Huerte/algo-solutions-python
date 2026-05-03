# Valid Number

class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            s = s.lower().strip()
            return 'inf' not in s and 'nan' not in s
        except:
            return False
    
s = Solution()
print(s.isNumber(" 005047e+6")) # True
print(s.isNumber("95a54e53"))   # False
print(s.isNumber("+6e-1"))      # True
print(s.isNumber("."))          # False