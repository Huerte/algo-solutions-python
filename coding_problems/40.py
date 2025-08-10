# 📜 Problem — Sum of Multiples of 3 and 5
# Description:
# Given a limit n, find the sum of all numbers from 0 to n-1 that are multiples of 3 or 5.
# This is a classic problem similar to Project Euler Problem 1.
# 
# Example:
# - Input: n = 10 → Output: 3 + 5 + 6 + 9 = 23
# - Input: n = 1000 → Output: sum of all multiples of 3 or 5 below 1000
# 
# Status: ✅ SOLVED

def sum_multiples_3_5(limit):
    if limit <= 0:
        return 0
    
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

# Test cases with assertions
assert sum_multiples_3_5(10) == 3 + 5 + 6 + 9  # 23
assert sum_multiples_3_5(20) == 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18  # 78
assert sum_multiples_3_5(1) == 0  # No multiples below 1
assert sum_multiples_3_5(6) == 3 + 5  # 8
assert sum_multiples_3_5(0) == 0
assert sum_multiples_3_5(1000) == 233168  # Classic Project Euler result

print("All test cases passed!")