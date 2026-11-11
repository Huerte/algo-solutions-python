# CodeWars -Pyramid Array
# Problem: Pyramid Array
# Source: https://www.codewars.com/kata/515f51d438015969f7000013
# Note: Generates a nested array with rows containing increasing numbers of 1s, from 1 to n.
def pyramid(n):
    res = []
    for i in range(1, n + 1):
        temp = []
        for j in range(i):
            temp.append(1)
        res.append(temp)
    return res

print(pyramid(0)) # []
print(pyramid(1)) # [[1]]
print(pyramid(3)) # [[1], [1, 1], [1, 1, 1]]
