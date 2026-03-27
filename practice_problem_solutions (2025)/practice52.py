# 📜 Problem — Equal and Divisible Pairs
# Description:
# Given an array of integers and an integer k, return the number of pairs (i, j) where:
# - 0 <= i < j < arr.length
# - arr[i] == arr[j]
# - (i * j) is divisible by k
#
# Input:
# - An array of integers `arr`
# - An integer `k` representing the divisor
#
# Output:
# - An integer representing the count of valid pairs
#
# Status: ✅ SOLVED

def equalDivisiblePairs(arr, k):
    if not arr or len(arr) < 2:
        return 0
        
    count_valid_pairs = 0
    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] == arr[j]) and (i * j) % k == 0:
                count_valid_pairs += 1
    
    return count_valid_pairs

# Test cases with assertions
# Example 1
arr1 = [3, 1, 2, 2, 2, 1, 3]
k1 = 2
assert equalDivisiblePairs(arr1, k1) == 4

# Example 2
arr2 = [1, 2, 3, 4]
k2 = 1
assert equalDivisiblePairs(arr2, k2) == 0

# Example 3
arr3 = [1, 1, 1, 1]
k3 = 1
assert equalDivisiblePairs(arr3, k3) == 6

# Example 4
arr4 = [1, 2, 1, 2]
k4 = 2
assert equalDivisiblePairs(arr4, k4) == 1

# Edge cases
arr5 = []
k5 = 1
assert equalDivisiblePairs(arr5, k5) == 0

arr6 = [1]
k6 = 1
assert equalDivisiblePairs(arr6, k6) == 0

print("All test cases passed!")