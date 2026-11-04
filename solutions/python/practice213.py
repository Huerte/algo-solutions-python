# CodeWars - Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# Problem: Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# Source: https://www.codewars.com/kata/5626b561280a42ecc50000d1
# Note: Finds numbers in a given range whose digits raised to consecutive powers sum to the original number.
def sum_dig_pow(a, b):
    res = []
    for i in range(a, b + 1):
        temp = sum(int(num) ** (j + 1) for j, num in enumerate(str(i)))
        if temp == i:
            res.append(i)
    return res

print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(90, 100))
