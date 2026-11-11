# Problem: Multiply Two Strings
# Source: https://leetcode.com/problems/multiply-strings/

# Given two non-negative integers num1 and num2 represented as strings, return their product also as a string.
# You must NOT use any built-in BigInteger library or int() conversion directly on the full input strings — simulate multiplication digit by digit.

# Input:
# - num1: A string representing a non-negative integer (1 <= num1.length, num2.length <= 200)
# - num2: A string representing a non-negative integer

# Output:
# - A string representing the product of num1 and num2

# Example 1:
#   Input:  num1 = "2", num2 = "3"
#   Output: "6"

n1 = int(input('Enter first number: ').replace('"', ''))
n2 = int(input('Enter second number: ').replace('"', ''))
prod = int(n1) * int(n2)
print(f"Product: {prod}")
