# 📜 Problem — Largest Number At Least Twice of Others
# Description:
# Given an array of integers, return the index of the largest element if it is at least twice as much
# as every other number in the array. If no such element exists, return -1.
# 
# Example:
# - Input: [3, 6, 1, 0] → Output: 1 (6 is largest and 6 >= 2*3, 6 >= 2*1, 6 >= 2*0)
# - Input: [1, 2, 3, 4] → Output: -1 (4 is not >= 2*3)
# 
# Status: ✅ SOLVED

def getMaxTwice(arr):
    if len(arr) <= 1:
        return -1

    # Find the maximum value and its index
    max_index = 0
    max_value = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    # Check if max_value is at least twice of all other elements
    for i in range(len(arr)):
        if i != max_index and arr[i] * 2 > max_value:
            return -1
    
    return max_index

# Test cases with assertions
assert getMaxTwice([3, 6, 1, 0]) == 1
assert getMaxTwice([1, 2, 3, 4]) == -1
assert getMaxTwice([1]) == -1
assert getMaxTwice([0, 0, 0, 1]) == 3
assert getMaxTwice([1, 0]) == 0
assert getMaxTwice([2, 4, 8, 16]) == -1

print("All test cases passed!")