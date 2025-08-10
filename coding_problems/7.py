# 📜 Problem — Integer to Roman
# Description:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given an integer, convert it to a roman numeral.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# Input:
# - An integer `num` where 1 <= num <= 3999
#
# Output:
# - A string representing the roman numeral
#
# Status: 🔄 IN PROGRESS - Needs fixing

class Solution(object):
    def intToRoman(self, num):
        # Define the mapping of integers to roman numerals
        roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ""
        
        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value
                
        return result

# Test cases with assertions
sol = Solution()

# Example 1
assert sol.intToRoman(3) == "III"

# Example 2
assert sol.intToRoman(4) == "IV"

# Example 3
assert sol.intToRoman(9) == "IX"

# Example 4
assert sol.intToRoman(58) == "LVIII"

# Example 5
assert sol.intToRoman(1994) == "MCMXCIV"

# Example 6
assert sol.intToRoman(10) == "X"

# Edge cases
assert sol.intToRoman(1) == "I"
assert sol.intToRoman(3999) == "MMMCMXCIX"

print("All test cases passed!")