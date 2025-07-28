n = int(input())
arr = []
for i in range(n):
    arr.append([int(j) for j in input().split()])

if len(arr) < 2:
    print("Not enough points")
else:
    distances = []

    for i in range(len(arr) - 1):
        r = (((arr[i + 1][0] ** 2) - (arr[i][0] ** 2)) + ((arr[i + 1][1] ** 2) - (arr[i][1] ** 2))) ** 0.5
        distances.append(r)

    distances = distances.sort()
    print()


"""
You need to solve the following problem: find the closest pair of points in two-dimensional space using Euclidean distance.

Your task is to write a program that takes input, finds the nearest pair of points, and output their coordinates according to the output description.
Input
Line 1: Integer N - the number of points to compare.
Next N lines: Each line contains two integers separated by a space, x and y - the coordinates of the points.
Output
Line 1: Coordinates of the point from the nearest pair of points in the same order as specified in the input data.
Line 2: Coordinates of the other point from the nearest pair of points.

If there are less than two points in the set: Not enough points
Constraints
N, x, y - integer
Example
Input
2
0 0
1 1
Output
0 0
1 1
"""