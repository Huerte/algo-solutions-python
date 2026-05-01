# GeeksforGeeks - Row with max 1s

class Solution:
    def rowWithMax1s(self, arr):
        max_ones = 0
        ind = -1
        
        for i, row in enumerate(arr):
            counts = row.count(1)
            if counts > max_ones:
                max_ones = counts
                ind = i
        
        return ind

s = Solution()
print(s.rowWithMax1s([[0, 1, 1], [0, 0, 1], [1, 1, 1]]))  # 2
print(s.rowWithMax1s([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # -1
print(s.rowWithMax1s([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))  # 0