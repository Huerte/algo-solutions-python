# HackerRank - Find Digits

def findDigits(n):
    div = n
    count = 0
    while n > 0:
        cur = n % 10
        if cur != 0 and div % cur == 0:
            count += 1
        n //= 10
    
    return count

print(findDigits(12)) # 2