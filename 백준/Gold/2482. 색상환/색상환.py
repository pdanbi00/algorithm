N = int(input())
K = int(input())
mod = 1000000003

# dp[i][j] : 1 ~ i번째 색만 가지고 인접하지 않게 j개의 색을 선택하는 경우의 수
# dp[i][j] : dp[i-1][j] + dp[i-2][j-1]
# i번째 색을 포함시키지 않고 j개의 색을 선택하는 경우의 수 : dp[i-1][j]
# i번째 색을 포함시키고 j개의 색을 선택하는 경우의 수 : dp[i-2][j-1]

# 원형 dp이기 때문에 마지막 N번째 색을 추가할 때는 예외 조건이 필요
#   N번째 색을 선택하는 경우 N-1번째랑 1번째 색 사용 불가능이기 때문에 dp[i-3][j-1]로 점화식 사용해야 됨.
#   N번째 색을 포함시키지 않고 만드는 경우에는 1번째 색을 사용해도 되기 때문에 dp[i-1][j]

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if j == 0:
            dp[i][j] = 1
            continue
        if j == 1:
            dp[i][j] = i
            continue
        dp[i][j] += dp[i-1][j]
        if i != N:
            dp[i][j] += dp[i-2][j-1]
        else:
            dp[i][j] += dp[i-3][j-1]
        dp[i][j] %= mod
print(dp[N][K])