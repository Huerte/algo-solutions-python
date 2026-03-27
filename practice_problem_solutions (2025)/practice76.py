# 📜 Problem — Multiplicative Persistence
# Description:
# Given a positive integer n, repeatedly multiply its digits until you get a single digit.
# Return the number of steps it takes to reach a single digit.
# 
# Example:
# - Input: n = 39 → Output: 3 (3*9=27, 2*7=14, 1*4=4, so 3 steps)
# - Input: n = 999 → Output: 4 (9*9*9=729, 7*2*9=126, 1*2*6=12, 1*2=2, so 4 steps)
# 
# Status: ✅ SOLVED

from math import log10, ceil

def multiplicative_persistence(n):
    if n < 10:
        return 0
    
    steps = 0
    current = n
    
    while current >= 10:
        # Convert to digits and multiply
        product = 1
        temp = current
        while temp > 0:
            product *= temp % 10
            temp //= 10
        current = product
        steps += 1
    
    return steps

# Test cases with assertions
assert multiplicative_persistence(39) == 3
assert multiplicative_persistence(999) == 4
assert multiplicative_persistence(4) == 0
assert multiplicative_persistence(25) == 2  # 2*5=10, 1*0=0
assert multiplicative_persistence(10) == 1  # 1*0=0
assert multiplicative_persistence(1) == 0
assert multiplicative_persistence(123) == 1  # 1*2*3=6

print("All test cases passed!")