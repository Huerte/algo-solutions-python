# Problem: Even Fibonacci Numbers Sum
# Source: https://projecteuler.net/problem=2

def fibonacciEvenSum(limit):
    
    total = 0
    a, b = 0, 1

    while b <= limit:
        a, b = b, a + b
        if b % 2 == 0:
            total += b

    return total

print(fibonacciEvenSum(4_000_000))