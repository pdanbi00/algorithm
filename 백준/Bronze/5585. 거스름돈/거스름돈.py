cost = int(input())
money = 1000 - cost
coins = [500, 100, 50, 10, 5, 1]

ans = 0

for coin in coins:
    if money // coin >= 1:
        tmp = money // coin
        ans += tmp
        money -= tmp * coin
print(ans)