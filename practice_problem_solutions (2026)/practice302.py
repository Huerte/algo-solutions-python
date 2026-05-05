# CodeWars - Currying functions: multiply all elements in an array

def multiply_all(arr):
    return lambda n: [x * n for x in arr]

print(multiply_all([1, 2, 3])(4))  # [4, 8, 12] 
print(multiply_all([1, 2, 3])(3))  # [3, 6, 9]
print(multiply_all([1, 2, 3])(2))  # [2, 4, 6]