import math


def evenNumberDigits(n):
    count = 0
    for _ in range(n):
        num_count = math.ceil(math.log10(int(input()) + 1))
        if num_count % 2 == 0:
            count += 1
    return count

print(evenNumberDigits(int(input())))