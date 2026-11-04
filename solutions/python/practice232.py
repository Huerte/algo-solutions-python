# CodeWars - Validate Credit Card Number
# Problem: Validate Credit Card Number
# Source: https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
# Note: Validates a credit card number using the Luhn algorithm by doubling alternate digits and checking whether the final sum is divisible by 10.
def validate(n):
    digits = str(n)
    res = []
    count = 0
    l = len(digits)
    for i in range(l):
        if i % 2 == 0 and l % 2 == 0:
            res.append(int(digits[i]) * 2)
        elif i % 2 != 0 and l % 2 != 0:
            res.append(int(digits[i]) * 2)
        else:
            res.append(int(digits[i]))

    for i, digit in enumerate(res):
        temp = str(digit)
        while len(temp) > 1:
            temp = str(sum(int(c) for c in temp))
        res[i] = int(temp)
    return sum(res) % 10 == 0

print(validate(1230)) # True
print(validate(1714)) # False
print(validate(2121)) # True
print(validate(891)) # False
