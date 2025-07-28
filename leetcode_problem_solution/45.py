from math import log10, ceil

n = 39

while ceil(log10(n + 1)) > 1:
    m = 1
    while n > 0:
        print(f"{m} * {n % 10}")
        m *= n % 10
        n //= 10
    n = m
    
print(n)