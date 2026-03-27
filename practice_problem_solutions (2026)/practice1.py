# Maximum Area of Longest Diagonal Rectangle

n = int(input("Enter the number of rectangles: "))

max_dia, max_area = 0, 0
for i in range(n):
    h, w = map(int, input(f'Enter length and width for rectangle {i+1}: ').split())

    dia = int((pow(h, 2) + pow(w, 2)) ** 0.5)
    a = h * w

    max_dia = max(dia, max_dia)
    max_area = max(a, max_area)

print(f"The area of the rectangle with the longest diagonal is: {max_area}")