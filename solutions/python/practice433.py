# Problem: Minimum Number of Jumps
# Source: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
# Topic: Dynamic Programming, Greedy
# Status: IN PROGRESS

def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(n):
        farthest = max(farthest, i + arr[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
            if curr_end >= n - 1:
                break
        if i >= farthest:
            return -1

    return jumps

assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]) == 3
assert min_jumps([1, 4, 3, 2, 6, 7]) == 2
assert min_jumps([0, 10, 20]) == -1
