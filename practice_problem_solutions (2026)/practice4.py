# Sum of Multiples of 3, 5, or 7

n = int(input('Enter a positive integer n: '))
sums = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        sums += i

print(f'Sum of all integers: {sums}')