# 📜 Problem — Unique Paths
# Description:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot
# can take to reach the bottom-right corner.
#
# Input:
# - m: An integer representing the number of rows (1 <= m <= 100)
# - n: An integer representing the number of columns (1 <= n <= 100)
#
# Output:
# - An integer representing the number of unique paths
#
# Status: ✅ SOLVED

def uniquePaths(m, n):
    # Create a DP table
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Test cases with assertions
# Example 1
assert uniquePaths(3, 7) == 28

# Example 2
assert uniquePaths(3, 2) == 3

# Example 3
assert uniquePaths(7, 3) == 28

# Edge cases
assert uniquePaths(1, 1) == 1
assert uniquePaths(1, 10) == 1
assert uniquePaths(10, 1) == 1
assert uniquePaths(2, 2) == 2

print("All test cases passed!")