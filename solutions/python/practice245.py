# CodeWars - Product of consecutive Fib numbers
# Problem: Product of consecutive Fib numbers
# Source: https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# Note: Generates consecutive Fibonacci numbers until their product is greater than or equal to the target, then returns the pair and a boolean indicating whether the product matches.
def product_fib(_prod):
    a, b = 0, 1
    while a * b != _prod and a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]

print(product_fib(4895)) # [55, 89,  True]
print(product_fib(5895)) # [89, 144, False]
