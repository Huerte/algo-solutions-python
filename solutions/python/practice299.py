# HackerRank - Between Two Sets
# Problem: Between Two Sets
# Source: https://www.hackerrank.com/challenges/between-two-sets/problem
# Note: Counts integers that are divisible by every element in the first array and divide every element in the second array.
def getTotalX(a, b):
    ar = []
    for i in range(a[-1], b[0] + 1):
        div = True
        
        for num in a:
            if i % num != 0:
                div = False
                break
        if div:
            ar.append(i)

    inc = []
    for num in ar:
        div = True
        for n in b:
            if n % num != 0:
                div = False
                break
        if div:
            inc.append(num)
    
    return len(inc)

print(getTotalX([2,4], [16,32,96]))
