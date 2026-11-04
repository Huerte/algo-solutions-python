# 📜 Problem — N-Queens II
# Source: https://leetcode.com/problems/n-queens-ii/
# Note: Uses recursion and backtracking to count valid queen placements.
# Description:
# The N-Queens problem asks us to place N queens on an N x N chessboard
# so that no two queens can attack each other.
#
# This solution uses backtracking to find all valid arrangements.
# It places one queen in each row and checks whether the selected position
# is safe by examining its row, column, and diagonals.
# If the position is safe, it places the queen and moves to the next row.
# If a placement does not lead to a valid arrangement, it removes the queen
# and tries another column.
# Whenever queens are successfully placed in all N rows, the solution
# counter is increased.
#
# Input:
# - n: An integer representing the size of the chessboard (1 <= n <= 9)
#
# Output:
# - An integer representing the total number of distinct valid arrangements.
#
# Approach:
# - Use recursion to process the chessboard one row at a time.
# - Check whether each position is safe before placing a queen.
# - Use backtracking to undo placements and explore other possibilities.
# - Count an arrangement when all rows have been filled successfully.
#
# Time Complexity: O(N! * N) — upper-bound estimate for exploring placements.
# Space Complexity: O(N^2) — for storing the chessboard, excluding recursion.
#
# Status: SOLVED

def totalNQueens(n):
    def is_safe(board, row, col):
        # Check row
        for j in range(n):
            if board[row][j] == 'Q':
                return False
        
        # Check column
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        # Check diagonal (top-right to bottom-left)
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(board, row):
        if row == n:
            nonlocal count
            count += 1
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    
    count = 0
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return count

# Test cases with assertions
# Example 1
assert totalNQueens(4) == 2

# Example 2
assert totalNQueens(1) == 1

# Example 3
assert totalNQueens(2) == 0  # No solution for 2x2

# Additional test cases
assert totalNQueens(3) == 0  # No solution for 3x3
assert totalNQueens(5) == 10
assert totalNQueens(6) == 4

print("All test cases passed!")