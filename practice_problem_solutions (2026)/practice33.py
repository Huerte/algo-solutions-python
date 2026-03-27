# Smallest Even Multiple

n = int(input("Enter a positive integer: "))

i = 1
res = None
while True:
    if i % 2 == 0 and i % n == 0:
        res = i
        break
    i += 1
print(f"Result: {res}")