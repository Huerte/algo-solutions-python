# 📜 Problem — Spiral Matrix
# Description:
# Given an m x n matrix, return all elements of the matrix in spiral order.
# The spiral order starts from the top-left corner and goes clockwise.
#
# Input:
# - matrix: A 2D integer array where m == matrix.length and n == matrix[i].length
# - 1 <= m, n <= 10
# - -100 <= matrix[i][j] <= 100
#
# Output:
# - A list of integers representing the spiral order traversal
#
# Status: ✅ SOLVED

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# Test cases with assertions
# Example 1
assert spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

# Example 2
assert spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

# Edge cases
assert spiralOrder([[1]]) == [1]
assert spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]
assert spiralOrder([[1, 2, 3]]) == [1, 2, 3]
assert spiralOrder([[1], [2], [3]]) == [1, 2, 3]

print("All test cases passed!")
