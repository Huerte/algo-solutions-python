# Matrix Rotate 90deg clockwise

matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))

row = len(matrix)
column = len(matrix[0])

r = int(input()) % 4
for _ in range(r):
    result = [[0] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            result[j][row - 1 - i] = matrix[i][j]
    matrix = result

print('\n'.join(map(str, matrix)))