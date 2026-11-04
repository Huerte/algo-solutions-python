# CodeWars - Sum of Odd Cubed Numbers
# Problem: Sum of Odd Cubed Numbers
# Source: https://www.codewars.com/kata/580dda86c40fa6c45f00028a
# Note: Returns the sum of cubed odd integers, or None if the array contains a non-integer value.
def cube_odd(arr):
    res = 0
    
    for num in arr:
        if type(num) == int:
            if (num ** 3) % 2 != 0:
                res += num ** 3
        else:
            return None
    return res


print(cube_odd([1, 2, 3, 4, 5])) # 153
print(cube_odd([0, 1, False, 3, True, 5])) # None
print(cube_odd([1, 2, 3, 4, 5, '7'])) # None
