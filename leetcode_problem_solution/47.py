import math

def sum_digits(num: int) -> int:
    while math.ceil(math.log10(num + 1)) > 1:
        sums = 0
        while num > 0:
            sums += num % 10
            num //= 10
        num = sums
        print(num)
    return num

print(sum_digits(38))