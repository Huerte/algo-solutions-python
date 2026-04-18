# HackerRank - Electronics Shop

def getMoneySpent(keyboards, drives, b):
    prices = []
    for kb in sorted(keyboards)[::-1]:
        for d in sorted(drives)[::-1]:
            if kb + d <= b:
                prices.append(kb + d)
    return max(prices) if prices else -1

print(getMoneySpent([40,50,60], [5,8,12], 60)) # 58
print(getMoneySpent([3,1], [5,2,8], 10)) # 9