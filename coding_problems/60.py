# 📜 Problem — Permutation Sequence
# Description:
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123", "132", "213", "231", "312", "321"
# Given n and k, return the kth permutation sequence.
#
# Input:
# - n: An integer where 1 <= n <= 9
# - k: An integer where 1 <= k <= n!
#
# Output:
# - A string representing the kth permutation sequence
#
# Status: ✅ SOLVED

def getPermutation(n, k):
    # Calculate factorial for each number
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i
    
    # Create list of available numbers
    numbers = list(range(1, n + 1))
    result = []
    k -= 1  # Convert to 0-based indexing
    
    for i in range(n, 0, -1):
        index = k // factorial[i - 1]
        result.append(str(numbers[index]))
        numbers.pop(index)
        k %= factorial[i - 1]
    
    return ''.join(result)

# Test cases with assertions
# Example 1
assert getPermutation(3, 3) == "213"

# Example 2
assert getPermutation(4, 9) == "2314"

# Example 3
assert getPermutation(3, 1) == "123"

# Edge cases
assert getPermutation(1, 1) == "1"
assert getPermutation(2, 1) == "12"
assert getPermutation(2, 2) == "21"

print("All test cases passed!")
