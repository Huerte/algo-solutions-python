# CodeWars -Pyramid Array

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