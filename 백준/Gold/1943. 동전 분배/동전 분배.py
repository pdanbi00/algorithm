# DP

for _ in range(3):
    N = int(input())
    coins = []
    total_coin = 0
    for _ in range(N):
        coin, cnt = map(int, input().split())
        total_coin += coin * cnt
        coins.append((coin, cnt))
    # 홀수는 반으로 나눌 수 없음 -> 확인 안해봐도 됨
    if total_coin % 2 == 1:
        print(0)
        continue
    total_coin = total_coin // 2

    # dp[i] : 동전들로 i원 만들수 있는지 여부
    dp = [False] * (total_coin + 1)
    dp[0] = True

    answer = 0

    for coin, cnt in coins:
        # 뒤에서부터 탐색하면서 지불 가능한 액수 갱신
        for n in range(total_coin, coin-1, -1):
            if dp[n-coin]:
                for j in range(cnt):
                    if n + coin * j <= total_coin:
                        dp[n + coin * j] = True
                    else:
                        break
        if dp[-1]:
            answer = 1
            break
    print(answer)