N = int(input())
resistance = list(map(int, input().split()))

# DP...

dp = [[1e9] * 2 for _ in range(N)]
# dp[i][0] : i번째 학생을 단죄하지 않았을 경우 최소값
# dp[i][1] : i번째 학생을 단죄했을 경우 최소값

dp[0][0] = 0
dp[0][1] = resistance[0]

for i in range(1, N):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + resistance[i]

print(min(dp[N-1][0], dp[N-1][1]))