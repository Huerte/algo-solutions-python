# Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        romans = [
            ['M', 1000],
            ['CM', 900], ['D', 500], ['CD', 400],
            ['C', 100], ['XC', 90], ['L', 50],
            ['XL', 40], ['X', 10], ['IX', 9],
            ['V', 5], ['IV', 4], ['I', 1]
        ]

        res = ""

        for sym, val in romans:
            if num // val:
                count, num = divmod(num, val)
                res += sym * count
        
        return res

s = Solution()
print(s.intToRoman(1390)) # "MCCCXC"
print(s.intToRoman(79))   # "LXXIX"
print(s.intToRoman(3))    # "III"