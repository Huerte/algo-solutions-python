# CodeWars - Multiplication Table

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