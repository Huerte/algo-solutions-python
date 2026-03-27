# Spiral Matrix

def spiral_matrix_list(arr):
    
    res = []

    left, right = 0, len(arr[0]) - 1
    top, down = 0, len(arr) - 1

    while len(res) < len(arr) * len(arr[0]):
        for i in range(left, right + 1):
            res.append(arr[top][i])
        top += 1

        if len(res) < len(arr) * len(arr[0]):
            for i in range(top, down + 1):
                res.append(arr[i][right])
            right -= 1

        if len(res) < len(arr) * len(arr[0]):
            for i in range(right, left - 1, -1):
                res.append(arr[down][i])
            down -= 1
        
        if len(res) < len(arr) * len(arr[0]):
            for i in range(down, top - 1, -1):
                res.append(arr[i][left])
            left += 1

    return res
    

print(spiral_matrix_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # == [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiral_matrix_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])) # == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]