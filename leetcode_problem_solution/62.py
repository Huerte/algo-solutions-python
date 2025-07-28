f, e, h = map(int, input().split())

total = f

h -= 1
if h > 0:
    total += h * e

print(total)