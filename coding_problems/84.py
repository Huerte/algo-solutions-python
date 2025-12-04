# def rotate(lst, n):
#     """Rotate the elements of lst by n steps.

#     A positive n indicates a right rotation, while a negative n indicates a left rotation.

#     Args:
#         lst (list): The list to be rotated.
#         n (int): The number of steps to rotate the list.

#     Returns:
#         list: The rotated list.
#     """

#     if not lst:
#         return lst
    
#     arr = [0] * len(lst)

#     for i in range(len(lst)):
#         arr[(i + n) % len(lst)] = lst[i]
    
#     return arr

def rotate(arr, n):
    if not arr:
        return []
    
    res = [0] * len(arr)

    for i in range(len(arr)):
        res[(i + n) % len(arr)] = arr[i]
    
    return res

# --- TESTS ---

# 1. basic right rotation
assert rotate([1,2,3,4,5], 1) == [5,1,2,3,4]
assert rotate([1,2,3,4,5], 2) == [4,5,1,2,3]

# 2. basic left rotation (negative steps)
assert rotate([1,2,3,4,5], -1) == [2,3,4,5,1]
assert rotate([1,2,3,4,5], -2) == [3,4,5,1,2]

# 3. full cycle (rotation equals length)
assert rotate([1,2,3], 3) == [1,2,3]
assert rotate([1,2,3], -3) == [1,2,3]

# 4. rotation larger than list length
assert rotate([1,2,3], 4) == [3,1,2]
assert rotate([1,2,3], 5) == [2,3,1]
assert rotate([1,2,3], -4) == [2,3,1]

# 5. empty list
assert rotate([], 10) == []

# 6. single-element list
assert rotate([9], 3) == [9]

# 7. mixed data types
assert rotate(['a','b','c'], 1) == ['c','a','b']

# 8. zero rotation (no change)
assert rotate([10,20,30], 0) == [10,20,30]

print('Success')