# CodeWars - Area of a Square

from math import pi
def square_area(A):
    return round((4 * A ** 2) / pi ** 2, 2)

print(square_area(14.05)) # 80.0
print(square_area(2))     # 1.62
print(square_area(0))     # 0.0