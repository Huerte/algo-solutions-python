import math


def sumAlternatingDigit(n):
    digitNum = math.floor(math.log10(abs(n))) + 1
    sign = 1

    if digitNum % 2 == 0:
       sign = -1

    totalSum = []

    while n > 0:
        m = n % 10 * sign
        totalSum.append(m)
        n //= 10
        sign *= -1

    return sum(totalSum)

print(sumAlternatingDigit(4567))