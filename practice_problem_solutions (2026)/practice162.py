def zeros(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
    
print(zeros(6))          # 1
print(zeros(30))         # 7
print(zeros(1000000000)) # 249999998