# Shortest Escape Path

from collections import deque

r, c = map(int, input().split())
grid = [input() for _ in range(r)]

sr, sc = None, None
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'S':
            sr, sc = i, j
            break

queue = deque([(sr, sc, 0)])
seen = set()
seen.add((sr, sc))

paths = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    
    rd, cd, steps = queue.popleft()

    if grid[rd][cd] == 'E':
        print(steps)
        break
    
    for rw, rc in paths:
        rd, cd = rd + rw, cd + rc
        if 0 <= rd < r and 0 <= cd < c:
            if grid[rd][cd] not in seen and grid[rd][cd] != '#':
                seen.add((rd, cd))
                queue.append((rd, cd, steps + 1))
else:
    print('NO PATH FOUND')
