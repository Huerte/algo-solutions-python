# Problem: Minimum Operations to Reduce Number to One
# Source: https://www.geeksforgeeks.org/dsa/reduce-a-number-to-1-by-performing-given-operations/
# Note: Greedy loop: halve even numbers; for odd numbers subtract 1, unless (n - 1) / 2 is odd and not 1, where adding 1 reaches a shorter chain of halvings

n = int(input('Enter a positive integer: '))
op = 0
while n > 1:
    op += 1

    if n % 2 == 0:
        n //= 2
    else:
        if (n - 1) / 2 == 1 or (n - 1) / 2 % 2 == 0:
            n -= 1
        else:
            n += 1
print(f"Minimum number of operations: {op}")