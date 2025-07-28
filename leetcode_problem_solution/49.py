def sol(arr):
    l = sorted(arr[0])
    for i in arr[1:]:
        if sorted(i) != l:
            return False
    return True

print(sol([[1,2,3], [3,1,2], [2,3,1]]))

assert sol([[1,2,3], [3,1,2], [2,3,1]]) == True  # Basic test with small lists
assert sol([[1,2,3], [3,1,2], [2,3,4]]) == False  # One list has a different element
assert sol([[5, 10, 15], [10, 15, 5], [15, 5, 10]]) == True  # Different order but same elements
assert sol([[1,1,2], [2,1,1], [1,2,1]]) == True  # Lists contain duplicates
assert sol([[1,2,3,4], [4,3,2,1], [3,1,4,2]]) == True  # Slightly larger lists
assert sol([[1,2,3,4], [4,3,2,1], [3,1,4,5]]) == False  # Last list has a wrong element
assert sol([[7,8,9], [9,7,8], [8,9,7], [7,9,8]]) == True  # Four lists
assert sol([[1,2], [2,1], [1,2]]) == True  # Simple two-element lists
assert sol([[1,2], [1,3]]) == False  # One different list
assert sol([[1]]) == True  # Single list should always return True
assert sol([[1,1,1], [1,1,1], [1,1,1]]) == True  # All identical lists
assert sol([[1,1,2], [2,2,1], [1,2,1]]) == False  # One list has a different frequency
assert sol([[0,0,0], [0,0,0], [0,0,0]]) == True  # All zeros
assert sol([[1,2,3,4,5], [5,4,3,2,1], [3,4,1,2,5]]) == True  # Longer lists with same numbers
assert sol([[1,2,3,4,5], [5,4,3,2,1], [3,4,1,2,6]]) == False  # Last list has a wrong element
assert sol([[1]*1000, [1]*1000, [1]*1000]) == True  # Large identical lists
assert sol([[i for i in range(1000)], [i for i in range(999, -1, -1)], sorted([i for i in range(1000)])]) == True  # Large lists with the same elements in different order
assert sol([[1,2,3,4], [1,2,3,4], [1,2,3,5]]) == False  # Last list has one incorrect element
assert sol([[1,2,3,4,4], [1,2,3,4,4], [4,3,2,1,4]]) == True  # Lists with repeated elements in different order
assert sol([[1,2,3,4,5], [5,4,3,2,1], [1,2,3,4]]) == False  # One list is shorter

print("All test cases passed! 🚀")