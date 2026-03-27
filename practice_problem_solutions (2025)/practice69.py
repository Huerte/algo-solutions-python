# 📜 Problem — Fibonacci Sequence Generator
# Description:
# Generate the first n Fibonacci numbers starting from 0 and 1.
# Each number in the sequence is the sum of the two preceding ones.
#
# Input:
# - An integer `n` representing the number of Fibonacci numbers to generate
#
# Output:
# - A list containing the first n Fibonacci numbers
#
# Status: ✅ SOLVED

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[i] + fib[i + 1])
    
    return fib

# Test cases with assertions
# Example 1
assert generate_fibonacci(1) == [0]

# Example 2
assert generate_fibonacci(2) == [0, 1]

# Example 3
assert generate_fibonacci(5) == [0, 1, 1, 2, 3]

# Example 4
assert generate_fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

# Example 5
assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Edge cases
assert generate_fibonacci(0) == []
assert generate_fibonacci(-1) == []

print("All test cases passed!")