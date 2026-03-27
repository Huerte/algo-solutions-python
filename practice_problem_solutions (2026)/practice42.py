# Spiral Matrix 2

def spiralMatrix(n):
    
    left, right = 0, n - 1
    top, down = 0, n - 1

    iter = 1

    matrix = [[0] * n for _ in range(n)]


    while iter <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = iter
            iter += 1
        top += 1
        

        for i in range(top, down + 1):
            matrix[i][right] = iter
            iter += 1
        right -= 1 

        for i in range(right, left - 1, -1):
            matrix[down][i] = iter
            iter += 1 
        down -= 1

        for i in range(down, top - 1, -1):
            matrix[i][left] = iter
            iter += 1
        left += 1
    
    return matrix        


print(spiralMatrix(3)) # == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
