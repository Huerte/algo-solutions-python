# Pascal Triangle

n = int(input('Enter the number of rows: '))
for i in range(n):
    c = 1
    for j in range(i + 1):
        print(c, end=' ')
        c = c * (i - j) // (j + 1)
    print()