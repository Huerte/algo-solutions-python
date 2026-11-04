# Multiply Strings
# Problem: Multiply Strings
# Source: https://leetcode.com/problems/multiply-strings/
# Note: Multiplies two non-negative integers represented as strings and returns their product as a string.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f"{int(num1) * int(num2)}"
