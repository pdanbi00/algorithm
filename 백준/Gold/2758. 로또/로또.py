# dp[i][j] : i번째 자리가 j로 끝나는 경우의 수
# 점화식 : dp[i][j] : j-1이하의 i개 수를 만드는 방법(j 사용하지 않고 i개 수 만드는 방법) + j // 2 이하의 i-1개의 수 만드는 방법(j를 사용해서 i개 수 만드는 법)
dp = [[0] * 2001 for _ in range(11)]

for i in range(2001):
    dp[0][i] = 1

for i in range(1, 11):
    for j in range(1, 2001):
            dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(dp[n][m])