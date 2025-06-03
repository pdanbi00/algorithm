import sys
input = sys.stdin.readline
N, K = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(N)]

def cal_dist(a, b):
    result = 0
    for i in range(2):
        result += abs(points[a][i] - points[b][i])
    return result

dp = [[1e9] * (K+1) for _ in range(N)]
dp[0][-1] = 0

for i in range(N-1):
    for j in range(K+1):
        if dp[i][j] == 1e9:
            continue
        for k in range(j+1):
            if i + k + 1 >= N:
                break
            dp[i+k+1][j-k] = min(dp[i+k+1][j-k], dp[i][j] + cal_dist(i, i+k+1))
print(dp[-1][0])