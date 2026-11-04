# Maximum Subarray Sum

def maxSub(arr):
    cur_sum = []
    seen = []
    for i in range(len(arr)):
        if seen and seen[-1] > arr[i]:
            cur_sum.append(seen)
            seen = [arr[i]]
            continue
        seen.append(arr[i])
    if seen:
        cur_sum.append(seen)
    return max(cur_sum, key=lambda x: sum(x)) if cur_sum else []

print(maxSub([1,2,3,4,5,6,7,8,9]))
print(maxSub([1,2,3,4,1,7,8,9]))
