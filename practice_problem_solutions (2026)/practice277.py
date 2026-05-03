# Number of Islands

class Solution(object):
    def numIslands(self, grid):
        
        def flood(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            flood(i + 1, j)
            flood(i - 1, j)
            flood(i, j + 1)
            flood(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    flood(i, j)
        
        return count

s = Solution()
print(s.numIslands([["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]])) # 1
print(s.numIslands([["1","1","0","0","0"],
                      ["1","1","0","0","0"],
                      ["0","0","1","0","0"],
                      ["0","0","0","1","1"]])) # 3
print(s.numIslands([["1","1","1"],
                    ["0","1","0"],
                    ["1","1","1"]]))           # 1