# 📜 Problem — Smallest Multiple That is Even
# Description:
# Given a positive integer n, find the smallest multiple of n that is even. If n is already even,
# return n. If n is odd, return n * 2.
# 
# Example:
# - Input: n = 4 → Output: 4 (already even)
# - Input: n = 7 → Output: 14 (7 * 2 = 14, which is even)
# 
# Status: ✅ SOLVED

def smallest_even_multiple(n):
    if n <= 0:
        return 0
    
    if n % 2 == 0:
        return n
    else:
        return n * 2

# Test cases with assertions
assert smallest_even_multiple(4) == 4
assert smallest_even_multiple(7) == 14
assert smallest_even_multiple(1) == 2
assert smallest_even_multiple(10) == 10
assert smallest_even_multiple(15) == 30
assert smallest_even_multiple(0) == 0

print("All test cases passed!")
