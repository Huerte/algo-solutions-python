# Problem: Rotting Oranges
# Source: https://leetcode.com/problems/rotting-oranges/
# Topic: BFS, Matrix

from collections import deque

def oranges_rotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes if fresh == 0 else -1

assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert oranges_rotting([[0,2]]) == 0
