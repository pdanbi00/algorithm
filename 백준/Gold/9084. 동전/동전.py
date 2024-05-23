T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0]+ list(map(int, input().split()))
    money = int(input())

    # dp[i][j] : coins의 i번째 동전을 가지고 j원을 만들 수 있는 가지수. i가 커질수록 0번부터 i번째 동전까지 다 섞어서 사용하는거임

    dp = [[0] * (money+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1 # 동전 0개를 써서 0원을 만들 수 있음.

    for i in range(1, N+1):
        for j in range(1, money+1):
            dp[i][j] = dp[i-1][j] # 이전까지의 동전들로 만든 결과 가져오기
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    print(dp[N][money])