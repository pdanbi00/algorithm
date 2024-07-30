C, N = map(int, input().split())

# dp 가보자~~
cost_list = [list(map(int, input().split())) for _ in range(N)]

dp = [1e9] * (C+100)
dp[0] = 0
# dp[i] = i명 만드는 데에 드는 최소비용

for cost, num_people in cost_list:
    for i in range(num_people, C+100):
        dp[i] = min(dp[i-num_people] + cost, dp[i])
print(min(dp[C:]))