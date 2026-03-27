# 📜 Problem — N-Queens II
# Description:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens threaten each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Input:
# - n: An integer representing the size of the chessboard (1 <= n <= 9)
#
# Output:
# - An integer representing the number of distinct solutions
#
# Status: ✅ SOLVED

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