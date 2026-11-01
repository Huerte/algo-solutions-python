# Calculate Alternating Digit Sum
# Read the digits from left to right, adding the first, subtracting the next,
# and continuing to alternate. For example, 521 becomes 5 - 2 + 1 = 4.
# Time: O(d), where d is the number of digits.

n = int(input('Enter a positive integer: '))

plus = True
res = 0

for num in map(int, str(n)):
    res += num * 1 if plus else num * -1
    plus = not plus

print(f'Sum: {res}')