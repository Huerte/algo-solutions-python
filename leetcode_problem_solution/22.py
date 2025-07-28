# reversed a number without casting
import math

def reverseN(n: int):
    result = 0
    digitNum = math.ceil(math.log10(n + 1))
    while n > 0:
        result += (n % 10) * math.pow(10, digitNum - 1)
        n //= 10
        digitNum -= 1
    return math.trunc(result)

def reverseNOptimized(x: int):
    result = 0
    n = abs(x)
    while n > 0:
        result = result * 10 + (n % 10)
        n //= 10
    is_negative = x < 0
    return -result if is_negative else result

print(reverseN(123))
print(reverseN(146))
print(reverseN(135))

print(reverseNOptimized(123))
print(reverseNOptimized(146))
print(reverseNOptimized(135))
