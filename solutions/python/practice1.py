# 📜 Problem — N-Queens II
# Source: https://leetcode.com/problems/n-queens-ii/
# Topic: Recursion, Backtracking
#
# Why this solution?
# A brute-force approach would try every possible arrangement
# of queens, including invalid arrangements.
#
# How does it solve the problem?
# This solution uses backtracking to place one queen in each row.
# Before placing a queen, it checks whether the selected position
# is safe from attacks in the same row, column, and diagonals.
# If a position is safe, it places the queen and recursively
# explores the next row.
#
# If a placement leads to a dead end, the queen is removed
# and another position is explored.
#
# Why backtracking?
# It avoids exploring arrangements that violate the rules,
# making the search more efficient than checking every arrangement.
#
# Input:
# - n: Size of the n x n chessboard (1 <= n <= 9)
#
# Output:
# - Integer representing the total number of valid arrangements.
#
# Complexity:
# - Time: Exponential in the number of rows in the worst case.
# - Space: O(n²) for the chessboard, plus recursion stack.
#
# Status: ✅ SOLVED
