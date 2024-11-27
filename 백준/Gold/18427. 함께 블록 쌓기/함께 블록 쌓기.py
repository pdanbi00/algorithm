# dp[i][j] : i번째 사람까지 계산한 j

N, M, H = map(int, input().split())
block = [[0] + list(map(int, input().split())) for _ in range(N)] # 블록을 사용안하는 경우도 포함하기 위해서 [0] + 를 사용
MOD = 10007
dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for h in range(H+1):
        if dp[i][h]:
            for j in block[i]:
                if h + j <= H:
                    dp[i+1][h+j] = (dp[i][h] + dp[i+1][h+j]) % MOD

    # for p in range(N+1):
    #     print(dp[p])
    # print('--------')
print(dp[N][H])