#largest number at least twice of others
def getMaxTwice(n):
    if n <= 1:
        return -1

    arr = []
    for _ in range(n):
        arr.append(int(input()))


    a, b = 0, 0
    #max_value = [0, 0]
    for i in range(n):
        if arr[i] > b:
            a, b = i, arr[i]

    if arr[a] >= arr[a - 1] * 2:
        return a

    return -1

print(getMaxTwice(4))