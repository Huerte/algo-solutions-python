# HackerRank - Equalize the Array

def equalizeArray(arr):
    return len(arr) - arr.count(max(arr, key=lambda x: arr.count(x)))

print(equalizeArray([3,3,2,1,3]))       # 2
print(equalizeArray([1,2,3,1,2,3,3,3])) # 4