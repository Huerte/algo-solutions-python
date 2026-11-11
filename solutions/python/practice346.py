# Geeksforgeeks - Binary to Decimal
# Problem: Binary to Decimal
# Source: https://www.geeksforgeeks.org/problems/binary-number-to-decimal-number3525/1
# Note: Converts a binary number represented as a string into its decimal equivalent using Python's int() function.
class Solution:
    def binary_to_decimal(self, B):
        return int(B, 2)

s = Solution()
print(s.binary_to_decimal("101"))  # 5
print(s.binary_to_decimal("1001")) # 9
print(s.binary_to_decimal("1111")) # 15
