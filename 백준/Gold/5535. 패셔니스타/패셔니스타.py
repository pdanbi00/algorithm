import sys
input = sys.stdin.readline
D, N = map(int, input().split())

temp = [int(input()) for _ in range(D)]
info = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : i날에 j번째 옷을 입었을 경우 최대 화려함
dp = [[0] * N for _ in range(D)]

for i in range(1, D):
    for j in range(N):
        if info[j][0] <= temp[i] <= info[j][1]:
            for k in range(N):
                if info[k][0] <= temp[i-1] <= info[k][1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(info[j][2] - info[k][2]))

print(max(dp[D-1]))