import sys

arr = [2, 7, 11, 15, 3, 5, 10, 12]
t = 17
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == t:
            print([i, j])
            sys.exit()