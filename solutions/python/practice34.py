def sort012(arr):
    res = []
    for i in range(3):
        res += [i] * arr.count(i)
    return res


print(sort012([0, 1, 2, 0, 1, 2]))

# Test cases
assert sort012([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
assert sort012([2, 1, 0]) == [0, 1, 2]
assert sort012([1, 1, 0, 2, 2, 0]) == [0, 0, 1, 1, 2, 2]
assert sort012([0, 0, 0]) == [0, 0, 0]
assert sort012([]) == []

print("All test cases passed!")
