# 📜 Problem — Spiral Matrix II
# Description:
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2
# in spiral order, starting from the top-left corner and going clockwise.
#
# Input:
# - n: A positive integer where 1 <= n <= 20
#
# Output:
# - A 2D integer array representing the spiral matrix
#
# Status: ✅ SOLVED

def generateMatrix(n):
    if n <= 0:
        return []
    
    # Initialize matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define boundaries
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Fill top row from left to right
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Fill right column from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Fill bottom row from right to left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        
        # Fill left column from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix

# Test cases with assertions
# Example 1
result_3 = generateMatrix(3)
expected_3 = [[1,2,3],[8,9,4],[7,6,5]]
assert result_3 == expected_3

# Example 2
result_1 = generateMatrix(1)
assert result_1 == [[1]]

# Additional test cases
result_2 = generateMatrix(2)
expected_2 = [[1,2],[4,3]]
assert result_2 == expected_2

result_4 = generateMatrix(4)
expected_4 = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
assert result_4 == expected_4

print("All test cases passed!")