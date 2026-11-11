# CodeWars - Currying functions: multiply all elements in an array
# Problem: Currying functions: multiply all elements in an array
# Source: https://www.codewars.com/kata/586909e4c66d18dd1800009b
# Note: Returns a function that multiplies every element of the original array by a given integer.
def multiply_all(arr):
    return lambda n: [x * n for x in arr]

print(multiply_all([1, 2, 3])(4))  # [4, 8, 12] 
print(multiply_all([1, 2, 3])(3))  # [3, 6, 9]
print(multiply_all([1, 2, 3])(2))  # [2, 4, 6]
