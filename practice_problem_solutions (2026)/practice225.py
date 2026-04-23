# HackerRank - Cut the sticks

def cutTheSticks(arr):
    count = [len(arr)]
    
    while arr:
        temp = []
        mn = min(arr)
        for i in range(len(arr)):
            if arr[i] - mn > 0:
                temp.append(arr[i] - mn)
        arr = temp
        if arr:
            count.append(len(arr))
    
    return count

print(cutTheSticks([5,4,4,2,2,8]))     # [6,4,2,1]
print(cutTheSticks([1,2,3,4,3,3,2,1])) # [8,6,4,1]