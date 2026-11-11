# Problem: Count Numbers with Unique Digits
# Source: https://leetcode.com/problems/count-numbers-with-unique-digits/

# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.
# This implementation brute-forces every number from 0 to 10^n - 1 and checks whether its decimal representation has all distinct digits.

# Input:
# - n: An integer representing the digit-length bound (0 <= n <= 8)
# Output:
# - An integer representing how many numbers in [0, 10^n) have all unique digits
#
# Example
#   Input:  n = 2
#   Output: 91
#   Explanation: Count numbers 0..99 with unique digits. Only 11, 22, ..., 99  are excluded -> 100 - 9 = 91.

n = int(input('Enter an integer: '))
ctr = 0
digits_range = int('9' * n)
for i in range(digits_range + 1):
    temp = str(i)
    if len(set(temp)) == len(temp):
        ctr += 1

print(f'Count of numbers with unique digits from 0 to {digits_range}: {ctr}')
