# 📜 Problem — Find the nth Prime Number
# Description:
# Given a positive integer n, find the nth prime number. A prime number is a natural number greater
# than 1 that has no positive divisors other than 1 and itself.
# 
# Example:
# - Input: n = 1 → Output: 2 (first prime number)
# - Input: n = 6 → Output: 13 (6th prime number: 2, 3, 5, 7, 11, 13)
# - Input: n = 10001 → Output: 104743 (10,001st prime number)
# 
# Status: ✅ SOLVED

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    if n <= 0:
        return None
    
    if n == 1:
        return 2
    
    count = 1
    num = 3
    
    while count < n:
        if is_prime(num):
            count += 1
        num += 2
    
    return num - 2

# Test cases with assertions
assert nth_prime(1) == 2
assert nth_prime(6) == 13
assert nth_prime(10) == 29
assert nth_prime(100) == 541
assert nth_prime(0) == None
assert nth_prime(-1) == None

print("All test cases passed!")