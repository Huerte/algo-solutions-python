# Merge Intervals

def intervals(arr):
    arr = sorted(arr, key=lambda x: x[0])
    new_arr = [arr[0]]
    
    for i in range(1, len(arr)):
        cur = arr[i]
        last = new_arr[-1]

        if cur[0] <= last[1]:
            last[1] = max(last[1], cur[1])
        else:
            new_arr.append(cur)

    return new_arr

print(intervals([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]

