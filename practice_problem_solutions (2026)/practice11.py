# Number of Steps to Reduce a Number to Zero

n = int(input('Enter an integer: '))

stp = 0

while n > 0:
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
    stp += 1

print(f'Number of steps to reduce N to 0: {stp}')