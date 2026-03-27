# Sliding window - longest subarray with sum <= S

n = int(input())
arr = [int(i) for i in input().split()][:n]

s = int(input())

res = []

for num in arr:
    if not res:
        res.append(num)
    
    elif sum(res) + num <= s:
        res.append(num)
    else:
        largest = max(res)
        if num < largest:
            res[res.index(largest)] = num

print(len(res))