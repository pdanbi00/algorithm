def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
        
    for coin in money:
        for price in range(coin, n+1):
            dp[price] = (dp[price] + dp[price-coin]) % 1000000007
    return dp[n]