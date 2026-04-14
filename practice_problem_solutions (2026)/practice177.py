# Matrix Diagonal Sum

class Solution(object):
    def diagonalSum(self, mat):
        tot = 0

        for i in range(len(mat)):
            tot += mat[i][i]
            tot += mat[i][len(mat)-1-i]
        
        if len(mat) % 2 != 0:
            tot -= mat[len(mat)//2][len(mat)//2]
        
        return tot

s = Solution()
print(s.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]])) # 55
print(s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]])) # 25
print(s.diagonalSum([[5]])) # 5