N = int(input())
nums = list(map(int, input().split()))

# dp : 수열의 역순으로 i번째까지와 순서대로 j번째까지의 최장공통수열 길이를 저장
# dp[i][j] : 역순으로 i번째까지의 수와 순서대로 j번째까지의 수의 최장 공통 수열 길이
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if nums[-i] == nums[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(N - dp[N][N])