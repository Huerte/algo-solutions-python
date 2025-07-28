class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [1]

        triangle = [[1], [1, 1]]

        for i in range(numRows - 2):  # for rows loop
            current_row_content = [1]
            for j in range(len(triangle[-1]) - 1):
                current_row_content.append(triangle[-1][j] + triangle[-1][j + 1])
                print(triangle[-1][j] + triangle[-1][j + 1], end=", ")
                j += 1
            current_row_content.append(1)
            print("\nrows: " + str(current_row_content))
            triangle.append(current_row_content)

        return triangle

sol = Solution()
for val in sol.generate(2):
    print(val)