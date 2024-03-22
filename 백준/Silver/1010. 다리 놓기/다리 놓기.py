# 조합을 dp로 풀기
T = int(input())
dp = [[0]*30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1: # mC1인 경우 m개의 경우가 있음
            dp[i][j] = j
        elif i == j: # mCm의 경우 1가지 경우가 있음
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])