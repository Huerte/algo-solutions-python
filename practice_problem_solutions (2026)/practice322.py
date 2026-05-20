# CodeChum - Longest subarray with sum k

ln, r = map(int, input().split())
arr = list(map(int, input().split()[:ln]))

seen = []

for i in range(ln - 1):
    for j in range(i + 1, ln):
        if sum(arr[i:j+1]) == r:
            seen.append(len(arr[i:j+1]))

print(min(seen) if seen else 0)
