# Coin Change (Minimum Coins)

def change(n):
    coins = [50, 20, 10, 5, 1]
    change = []
    while n > 0:
        for coin in coins:
            if coin <= n:
                n -= coin
                change.append(coin)
                break
    return change


print(change(25))
print(change(15))
print(change(45))