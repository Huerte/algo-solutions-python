# CodeWars - N-th Fibonacci
# Problem: N-th Fibonacci
# Source: https://www.codewars.com/kata/522551eee9abb932420004a0
# Note: Calculates the N-th Fibonacci number iteratively using two variables to track the previous two values.
def nth_fib(n):
    a, b = 0, 1
    count = 2
    if n < 2:
        return [a, b][n - 1]
    while count < n:
        a, b = b, a + b
        count += 1
    return b

print(nth_fib(1)) # 0
print(nth_fib(2)) # 1
print(nth_fib(100)) # 218922995834555169026
