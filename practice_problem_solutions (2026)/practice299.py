# HackerRank - Running Time of Algorithms

def runningTime(arr):
    count = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            count += 1
            j -= 1
        arr[j + 1] = key
    
    return count

print(runningTime([ 8, 6, 6, 42, 8, 1, 1, 13, 4, 6, 2, 1, 1, 39 ])) # 51
print(runningTime([2, 1, 3, 1, 2]))                                 # 4
print(runningTime([1, 1, 1, 2, 2]))                                 # 0