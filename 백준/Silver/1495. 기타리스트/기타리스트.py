N, S, M = map(int, input().split())
volume = list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
# dp[i][j] : i번째 곡을 j만큼의 볼륨으로 연주할 수 있는지 여부

dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] > 0:
            if (0 <= j + volume[i-1] <= M):
                dp[i][j+volume[i-1]] = 1
            if (0 <= j - volume[i-1] <= M):
                dp[i][j-volume[i-1]] = 1

answer = -1
for i in range(M+1):
    if dp[N][i] == 1:
        answer = i
print(answer)