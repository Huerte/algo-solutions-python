# Longest Increasing Subsequence

def lis(arr):
    ar = []

    for i in range(len(arr) - 1):
        temp = [arr[i]]
        for j in range(i + 1, len(arr)):
            if temp[-1] < arr[j]:
                temp.append(arr[j])
            else:
                temp[-1] = arr[j]
        ar.append(temp)

    return len(max(ar, key=len))

print(lis([3,1,8,2,5]))       # 3
print(lis([5,2,8,6,3,6,9,5])) # 4