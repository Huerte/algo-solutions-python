# Calculate Alternating Digit Sum

n = int(input('Enter a positive integer: '))

plus = True
res = 0

for num in map(int, str(n)):
    res += num * 1 if plus else num * -1
    plus = not plus

print(f'Sum: {res}')