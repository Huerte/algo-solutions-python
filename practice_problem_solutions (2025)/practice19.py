# 📜 Problem — Minimum Path Sum
# Description:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
#
# Input:
# - grid: A 2D integer array where m == grid.length and n == grid[i].length
# - 1 <= m, n <= 200
# - 0 <= grid[i][j] <= 100
#
# Output:
# - An integer representing the minimum path sum
#
# Status: ✅ SOLVED

def minPathSum(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    # Create DP table
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Test cases with assertions
# Example 1
grid1 = [[1,3,1],[1,5,1],[4,2,1]]
assert minPathSum(grid1) == 7

# Example 2
grid2 = [[1,2,3],[4,5,6]]
assert minPathSum(grid2) == 12

# Edge cases
grid3 = [[1]]
assert minPathSum(grid3) == 1

grid4 = [[1, 2], [3, 4]]
assert minPathSum(grid4) == 7

print("All test cases passed!")
