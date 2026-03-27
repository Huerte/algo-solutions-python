# 📜 Problem — Non-Unique Elements
# Description:
# Given an array of integers, return a new array containing only the elements that 
# appear more than once in the original array. The order of elements should be preserved.
#
# Input:
# - An array of integers `data`
#
# Output:
# - An array containing only the non-unique elements in their original order
#
# Status: ✅ SOLVED

from collections.abc import Iterable

def checkio(data: list[int]) -> Iterable[int]:
    unique = set(data)
    result = []
    for item in unique:
        if data.count(item) == 1:
            result.append(item)
    return [x for x in data if x not in result]

# Test cases with assertions
print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

#These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("All test cases passed!")
