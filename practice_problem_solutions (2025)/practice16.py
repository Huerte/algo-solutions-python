# 📜 Problem — Rank Transform Array
# Description:
# Given an array of integers, replace each element with its rank. The rank represents 
# how large the element is. The rank has the following rules:
# - Rank 1 is the smallest element
# - Rank 2 is the second smallest element
# - And so on...
# - Equal elements get the same rank
#
# Input:
# - An array of integers `arr`
#
# Output:
# - An array where each element is replaced by its rank
#
# Status: 🔄 IN PROGRESS - Incomplete implementation

def rankTransformArray(arr):
    if not arr:
        return []
    
    # Create a list of (value, index) pairs
    indexed_arr = [(val, i) for i, val in enumerate(arr)]
    
    # Sort by value
    indexed_arr.sort(key=lambda x: x[0])
    
    # Assign ranks
    ranks = [0] * len(arr)
    rank = 1
    
    for i in range(len(indexed_arr)):
        if i > 0 and indexed_arr[i][0] != indexed_arr[i-1][0]:
            rank = i + 1
        ranks[indexed_arr[i][1]] = rank
    
    return ranks

# Test cases with assertions
# Example 1
assert rankTransformArray([40, 10, 20, 30]) == [4, 1, 2, 3]

# Example 2
assert rankTransformArray([100, 100, 100]) == [1, 1, 1]

# Example 3
assert rankTransformArray([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]

# Example 4
assert rankTransformArray([1]) == [1]

# Edge cases
assert rankTransformArray([]) == []
assert rankTransformArray([5, 5, 5, 5]) == [1, 1, 1, 1]

print("All test cases passed!")