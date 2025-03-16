# W 한 개가 나와야 H가 나올 수 있음.
dp = [[0] * 31 for _ in range(31)]
for j in range(1, 31):
    dp[0][j] = 1
for i in range(1, 31):
    for j in range(i, 31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][N])
