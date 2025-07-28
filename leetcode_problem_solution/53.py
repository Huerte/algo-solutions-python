n = input()
j = int(n)

k = 0
while j % 1000 == 0 and j > 0:
    j //= 1000
    k += 1

print(f'{j:g}k{k}')