# maximum area of longest diagonal rectangle
from math import sqrt

max_area = 0
max_diagonal = 0
for _ in range(int(input())):
    l, b = [int(j) for j in input().split()]
    current_area = l * b
    current_diagonal = sqrt(l ** 2 + b ** 2)
    if current_diagonal > max_diagonal or (current_diagonal == max_diagonal and current_area > max_area):
        max_diagonal = current_diagonal
        max_area = current_area
print(max_area)