# 📜 Problem — Two Sum
# Description:
# Given an array of integers and a target sum, find two numbers in the array that add up to the target.
# Return the indices of these two numbers. You may assume that each input has exactly one solution.
# 
# Example:
# - Input: arr=[2, 7, 11, 15], target=9 → Output: [0, 1] (2 + 7 = 9)
# - Input: arr=[3, 2, 4], target=6 → Output: [1, 2] (2 + 4 = 6)
# 
# Status: ✅ SOLVED

def two_sum(arr, target):
    if not arr or len(arr) < 2:
        return []
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return []  # No solution found

# Test cases with assertions
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
assert two_sum([1, 2], 3) == [0, 1]
assert two_sum([1], 2) == []
assert two_sum([], 5) == []

print("All test cases passed!")