N = int(input())
trains = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    trains[i] += trains[i-1]
M = int(input())

# dp[i][j] : 소형기관차 i개까지 선택하고, j번째까지 객차 고래했을 때 최대 승객 수
dp = [[0] * (N+1) for _ in range(4)]

# 경우는 2가지
# 1. i번째 소형기관차까지 추가되었고, j번째 객차를 추가한 경우(j-M+1부터 j번까지 추가되는거임)
# 2. i번째 소형기관차까지 추가되었고, j번째 객차를 추가하지 않는 경우
for i in range(1, 4):
    for j in range(M*i, N+1):
        dp[i][j] = max(dp[i-1][j-M] + trains[j] - trains[j-M], dp[i][j-1])

print(dp[3][N])