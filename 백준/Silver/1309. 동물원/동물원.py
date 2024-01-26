# 가로 전체를 한번에 생각
# 0 : 양쪽 모두에 동물 없음
# 1 : 왼쪽에 동물
# 2 : 오른쪽에 동물

N = int(input())
dp = [[0] * 3 for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    dp[i][0] %= 9901
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][1] %= 9901
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
    dp[i][2] %= 9901
print(sum(dp[N]) % 9901)