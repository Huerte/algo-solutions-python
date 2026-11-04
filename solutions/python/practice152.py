# Largest Local Values in a Matrix
# Problem: Largest Local Values in a Matrix
# Source: https://leetcode.com/problems/largest-local-values-in-a-matrix/
# Note: Finds the maximum value in every contiguous 3x3 submatrix.

class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res
