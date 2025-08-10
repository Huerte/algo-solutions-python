# 📜 Problem — Average Without Min and Max
# Description:
# Given an array of integers, calculate the average of all elements except the minimum 
# and maximum values. The result should be formatted to two decimal places.
#
# Input:
# - An array of integers `arr` with at least 3 elements
#
# Output:
# - A float representing the average of elements excluding min and max
#
# Status: ✅ SOLVED

def averageWithoutMinMax(arr):
    if len(arr) < 3:
        return 0.0
        
    # Create a copy to avoid modifying the original array
    temp_arr = arr.copy()
    
    # Remove min and max
    temp_arr.remove(min(temp_arr))
    temp_arr.remove(max(temp_arr))
    
    # Calculate average
    average = sum(temp_arr) / len(temp_arr)
    return round(average, 2)

# Test cases with assertions
# Example 1
arr1 = [1, 2, 3, 4, 5]
assert averageWithoutMinMax(arr1) == 3.0

# Example 2
arr2 = [10, 20, 30, 40, 50]
assert averageWithoutMinMax(arr2) == 30.0

# Example 3
arr3 = [5, 5, 5, 5, 5]
assert averageWithoutMinMax(arr3) == 5.0

# Example 4
arr4 = [1, 10, 100]
assert averageWithoutMinMax(arr4) == 10.0

# Example 5
arr5 = [0, 1, 2, 3, 4, 5]
assert averageWithoutMinMax(arr5) == 2.5

# Edge cases
arr6 = [1, 2, 3]
assert averageWithoutMinMax(arr6) == 2.0

print("All test cases passed!")