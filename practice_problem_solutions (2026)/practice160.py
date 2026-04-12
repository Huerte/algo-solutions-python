# CodeWars - Product of consecutive Fib numbers

def product_fib(_prod):
    a, b = 0, 1
    while a * b != _prod and a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]

print(product_fib(4895)) # [55, 89,  True]
print(product_fib(5895)) # [89, 144, False]