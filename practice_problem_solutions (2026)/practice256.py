# Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        res = [[0] * n for _ in range(n)]
        cur = 1
        while cur < n * n + 1:

            for i in range(left, right + 1):
                res[top][i] = cur
                cur += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = cur
                cur += 1
            right -= 1

            for i in range(right, left-1, -1):
                res[bottom][i] = cur
                cur += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res[i][left] = cur
                cur += 1
            left += 1
            
        return res
    
s = Solution()

print(s.generateMatrix(4)) # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(s.generateMatrix(3)) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(s.generateMatrix(1)) # [[1]]