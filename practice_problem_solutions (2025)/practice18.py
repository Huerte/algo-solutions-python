# 📜 Problem — Unique Paths II
# Description:
# You are given an m x n integer array obstacleGrid. There is a robot initially located at
# the top-left corner (i.e., obstacleGrid[0][0]). The robot tries to move to the bottom-right
# corner (i.e., obstacleGrid[m-1][n-1]). The robot can only move either down or right at
# any point in time.
# An obstacle and space are marked as 1 or 0 respectively in obstacleGrid. A path that the
# robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# Input:
# - obstacleGrid: A 2D integer array where m == obstacleGrid.length and n == obstacleGrid[i].length
# - 1 <= m, n <= 100
# - obstacleGrid[i][j] is 0 or 1
#
# Output:
# - An integer representing the number of unique paths
#
# Status: ✅ SOLVED

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0]:
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # If start or end is blocked, return 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    
    # Create DP table
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    # Fill first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    # Fill first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Test cases with assertions
# Example 1
grid1 = [[0,0,0],[0,1,0],[0,0,0]]
assert uniquePathsWithObstacles(grid1) == 2

# Example 2
grid2 = [[0,1],[0,0]]
assert uniquePathsWithObstacles(grid2) == 1

# Edge cases
grid3 = [[1]]
assert uniquePathsWithObstacles(grid3) == 0

grid4 = [[0]]
assert uniquePathsWithObstacles(grid4) == 1

grid5 = [[0, 0], [0, 0]]
assert uniquePathsWithObstacles(grid5) == 2

print("All test cases passed!")