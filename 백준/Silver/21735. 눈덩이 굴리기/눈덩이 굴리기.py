N, M = map(int, input().split())
yard = [0] + list(map(int, input().split()))
dp = [[-1] * (N+1) for _ in range(M+1)]

answer = 1
dp[0][0] = 1
for i in range(M):
    for j in range(N):
        if dp[i][j] != -1:
            # 던지기
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + yard[j+1])

            # 굴리기
            if j+2 <= N:
                dp[i+1][j+2] = max(dp[i+1][j+2], dp[i][j] // 2 + yard[j+2])

for i in range(M+1):
    answer = max(answer, max(dp[i]))

print(answer)