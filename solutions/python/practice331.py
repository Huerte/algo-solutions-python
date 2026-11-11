# Problem: Circular Array Rotation
# Source: https://www.hackerrank.com/challenges/circular-array-rotation/problem
# Note: Rotate the array right by k positions (k reduced modulo the length), then answer each query by index

def circularArrayRotation(a, k, queries):
    k %= len(a)
    arr = a[-k:] + a[:-k]
    return [arr[i] for i in queries]

print(circularArrayRotation([1, 2, 3, 4], 4, [0, 1, 2, 3]))  # [1, 2, 3, 4]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))        # [2, 3, 1]
print(circularArrayRotation([3, 4, 5], 2, [1, 2]))           # [5, 3]


if __name__ == "__main__":
    # Plain right rotation: the last element wraps around to the front.
    assert circularArrayRotation([1, 2, 3], 1, [0, 1, 2]) == [3, 1, 2]

    # Edge case: zero rotations must leave the array unchanged.
    assert circularArrayRotation([1, 2, 3], 0, [0, 1, 2]) == [1, 2, 3]

    # Edge case: k equal to the array length is a full cycle, so nothing moves.
    assert circularArrayRotation([1, 2, 3], 3, [0, 1, 2]) == [1, 2, 3]

    # k larger than the length wraps around: 7 rotations of a 5-element
    # array behave like 2 rotations.
    assert circularArrayRotation([1, 2, 3, 4, 5], 7, [0, 3, 4]) == [4, 2, 3]

    # Edge case: a single-element array never changes, whatever k is.
    assert circularArrayRotation([9], 100, [0]) == [9]

    print("All test cases passed!")
