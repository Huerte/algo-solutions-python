# 📜 Problem — N-Queens
# Description:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens threaten each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Input:
# - n: An integer representing the size of the chessboard (1 <= n <= 9)
#
# Output:
# - A list of all distinct solutions, where each solution is a list of strings
# - Each string represents a row with 'Q' for queen and '.' for empty cell
#
# Status: ✅ SOLVED

def solveNQueens(n):
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
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result

# Test cases with assertions
# Example 1
solutions_4 = solveNQueens(4)
assert len(solutions_4) == 2
assert ['.Q..', '...Q', 'Q...', '..Q.'] in solutions_4
assert ['..Q.', 'Q...', '...Q', '.Q..'] in solutions_4

# Example 2
solutions_1 = solveNQueens(1)
assert len(solutions_1) == 1
assert solutions_1[0] == ['Q']

# Edge case
solutions_2 = solveNQueens(2)
assert len(solutions_2) == 0  # No solution for 2x2

print("All test cases passed!")