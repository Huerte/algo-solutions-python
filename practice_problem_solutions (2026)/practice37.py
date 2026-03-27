# Spiral Matrix Display

def spiral_display(arr):

    s = []

    n = len(arr)

    left, right = 0, n - 1
    top , down  = 0, n - 1

    while top <= down and left <= right:

        for i in range(left, right + 1):
            s.append(arr[top][i])
        top += 1

        for i in range(top, down + 1):
            s.append(arr[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            s.append(arr[down][i])
        down -= 1

        for i in range(down, top - 1, -1):
            s.append(arr[i][left])
        left += 1

    return ' '.join(map(str, s))


print(spiral_display([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]))