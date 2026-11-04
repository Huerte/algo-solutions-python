# 📜 Problem — N-Queens II
# Source: https://leetcode.com/problems/n-queens-ii/
# Topic: Recursion, Backtracking
#
# Why this solution?
# Brute force checks many possible queen arrangements,
# including invalid ones.
#
# How does it solve the problem?
# Backtracking places one queen in each row. Before placing
# a queen, it checks whether the position is safe from attacks
# in the same row, column, and diagonals.
#
# If a placement fails, it removes the queen and tries another
# position. This allows the algorithm to explore valid
# arrangements without keeping invalid placements.
#
# Why backtracking?
# It stops exploring a path as soon as a placement is invalid.
#
# Input:
# - n: Size of the n x n chessboard (1 <= n <= 9)
#
# Output:
# - Number of distinct valid arrangements.
#
# Complexity:
# - Time: Exponential in the worst case.
# - Space: O(n²) for the board, plus recursion stack.
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


# Test cases
assert totalNQueens(4) == 2
assert totalNQueens(1) == 1
assert totalNQueens(2) == 0
assert totalNQueens(3) == 0
assert totalNQueens(5) == 10
assert totalNQueens(6) == 4

print("All test cases passed!")
