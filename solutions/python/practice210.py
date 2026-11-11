# CodeWars - Multiplication Table
# Problem: Multiplication table
# Source: https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
# Note: Generates an N x N multiplication table using the multiples of each row number.
def multiplication_table(size):
    adder = 1
    arr = []
    for _ in range(size):
        arr.append(list(range(adder, adder * size + 1, adder)))
        adder += 1
    return arr

print(multiplication_table(1)) # [[1]]
print(multiplication_table(2)) # [[1, 2], [2, 4]]
print(multiplication_table(3)) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
