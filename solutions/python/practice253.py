# Number of Islands
# Problem: Number of Islands
# Source: https://leetcode.com/problems/number-of-islands/
# Note: Counts individual land cells ('1') in a 2D grid; the original problem requires counting connected groups of land using DFS or BFS.
def islands(arr):
    island = 0

    for ar in arr:
        for num in ar:
            if num == '1':
                island += 1
    
    return island


print(islands([['1','0','1'], ['1','1','1'], ['1','0','1']]))
