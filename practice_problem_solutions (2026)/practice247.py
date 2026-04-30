# HackerRank - Circular Array Rotation

def circularArrayRotation(a, k, queries):
    k %= len(a)
    arr = a[-k:] + a[:-k]
    return [arr[i] for i in queries]

print(circularArrayRotation([1, 2, 3, 4], 4, [0, 1, 2, 3]))  # [1, 2, 3, 4]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))        # [2, 3, 1]
print(circularArrayRotation([3, 4, 5], 2, [1, 2]))           # [5, 3]