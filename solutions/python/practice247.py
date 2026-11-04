# Problem: Number of trailing zeros of N!
# Source: https://www.codewars.com/kata/number-of-trailing-zeros-of-n
# Note: Counts the factors of 5 in N! to calculate its trailing zeros without computing the factorial.
def zeros(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
    
print(zeros(6))          # 1
print(zeros(30))         # 7
print(zeros(1000000000)) # 249999998
