# 📜 Problem — Count Numbers with Even Number of Digits
# Description:
# Given a list of numbers, count how many of them have an even number of digits.
# A number has an even number of digits if the count of its digits is divisible by 2.
#
# Input:
# - An integer n representing the number of numbers to check
# - n lines of integers to check
#
# Output:
# - An integer representing the count of numbers with even number of digits
#
# Status: ✅ SOLVED

import math

def evenNumberDigits(numbers):
    if not numbers:
        return 0
        
    count = 0
    for num in numbers:
        if num == 0:
            num_count = 1  # 0 has 1 digit
        else:
            num_count = math.floor(math.log10(abs(num))) + 1
            
        if num_count % 2 == 0:
            count += 1
    return count

# Test cases with assertions
# Example 1
numbers1 = [12, 345, 2, 6, 7896]
assert evenNumberDigits(numbers1) == 2  # 12 and 7896 have even digits

# Example 2
numbers2 = [555, 901, 482, 1771]
assert evenNumberDigits(numbers2) == 1  # Only 1771 has even digits

# Example 3
numbers3 = [1, 2, 3, 4, 5]
assert evenNumberDigits(numbers3) == 0  # All have odd digits

# Example 4
numbers4 = [10, 100, 1000]
assert evenNumberDigits(numbers4) == 3  # All have even digits

# Edge cases
numbers5 = []
assert evenNumberDigits(numbers5) == 0

numbers6 = [0]
assert evenNumberDigits(numbers6) == 0  # 0 has 1 digit (odd)

print("All test cases passed!")