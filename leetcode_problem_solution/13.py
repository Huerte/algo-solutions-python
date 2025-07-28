coord_x = []
coord_y = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    coord_x.append(x)
    coord_y.append(y)

cable_destination = max(coord_x) - min(coord_x)
median = None
coord_y.sort()
if len(coord_y) % 2 == 0:
    median = (coord_y[(len(coord_y) // 2)] + coord_y[(len(coord_y) // 2 + 1)]) // 2
else:
    median = coord_y[(len(coord_y) // 2 + 1)]

print(cable_destination + median)
