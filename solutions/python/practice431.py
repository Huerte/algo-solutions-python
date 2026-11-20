# Problem: Tribonacci Sequence
# Source: https://www.codewars.com/kata/556deca17c460c907e00000a
# Topic: Sequences, Math

def tribonacci(signature, n):
    if n <= 0:
        return []
    if n <= 3:
        return signature[:n]

    res = list(signature)
    for _ in range(n - 3):
        res.append(res[-1] + res[-2] + res[-3])
    return res

assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
assert tribonacci([1, 2, 3], 2) == [1, 2]
assert tribonacci([1, 2, 3], 0) == []
