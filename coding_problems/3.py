# 📜 Problem — Pascal's Triangle
# Description:
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Input:
# - An integer `numRows` where 1 <= numRows <= 30
#
# Output:
# - A list of lists representing Pascal's triangle
#
# Status: ✅ SOLVED

class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]

        for i in range(numRows - 2):  # for rows loop
            current_row_content = [1]
            for j in range(len(triangle[-1]) - 1):
                current_row_content.append(triangle[-1][j] + triangle[-1][j + 1])
            current_row_content.append(1)
            triangle.append(current_row_content)

        return triangle

# Test cases with assertions
sol = Solution()

# Example 1
assert sol.generate(1) == [[1]]

# Example 2
assert sol.generate(2) == [[1], [1, 1]]

# Example 3
assert sol.generate(3) == [[1], [1, 1], [1, 2, 1]]

# Example 4
assert sol.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

# Example 5
assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print("All test cases passed!")