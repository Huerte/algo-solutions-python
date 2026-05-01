# Geeksforgeeks - Binary to Decimal

class Solution:
    def binary_to_decimal(self, B):
        return int(B, 2)

s = Solution()
print(s.binary_to_decimal("101"))  # 5
print(s.binary_to_decimal("1001")) # 9
print(s.binary_to_decimal("1111")) # 15