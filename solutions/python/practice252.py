# FizzBuzz with Twist

def fizzbuzzpop(n):
    res = ""
    if n % 3 == 0:
        res += 'Fizz'
    if n % 5 == 0:
        res += 'Buzz'
    if n % 7 == 0:
        res += 'Pop'
    return res

print(fizzbuzzpop(9))
print(fizzbuzzpop(10))
print(fizzbuzzpop(15))
print(fizzbuzzpop(49))
