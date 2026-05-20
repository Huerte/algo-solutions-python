# Flood Fill

from collections import deque

def bfs(grid, seen, r, c, row, column):
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(r, c)])
    seen.add((r, c))

    while queue:

        rd, cd = queue.popleft()

        for dr, dc in dir:
            nr, nc = rd + dr, cd + dc
            if 0 <= nr < row and 0 <= nc < column:
                if (nr, nc) not in seen and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    seen.add((nr, nc))


row, column = map(int, input().split())
grid = [input() for _ in range(row)]
island = 0

seen = set()
for r in range(row):
    for c in range(column):
        if grid[r][c] == '1' and (r, c) not in seen:
            bfs(grid, seen, r, c, row, column)
            island += 1

print(island)