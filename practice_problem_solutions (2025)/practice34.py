def sort012(arr):
    res = []
    for i in range(3):
        res += [i] * arr.count(i)
    return res

print(sort012([0, 1, 2, 0, 1, 2]))