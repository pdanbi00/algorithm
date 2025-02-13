N = int(input())
power = list(map(int, input().split()))
happy = list(map(int, input().split()))

# dp[i][j] : 체력이 i인 상태에서 j번째 사람에게 인사를 했을 경우 얻을 수 있는 최대 기쁨

dp = [[0] * 101 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, 101):
        if j - power[i-1] > 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-power[i-1]] + happy[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][100])