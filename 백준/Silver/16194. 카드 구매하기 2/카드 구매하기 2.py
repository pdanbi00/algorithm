# 아이디어 : DP임
# n 개를 사는 방법 : (1개 사는 방법 + n-1개 사는 방법) + (2개 사는 방법 + n-2개 사는 방법) + ... + (n개 사는 방법)
# dp[i]를 i개를 사는 최소 비용
# dp[i] = dp[i-j] + card[j]
N = int(input())
card = list(map(int, input().split()))
dp = [0 for _ in range(N+1)] # dp[1] : 1개의 카드를 살 수 있는 최소 비용
for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] == 0:
            dp[i] = dp[i-j] + card[j-1]
        else:
            dp[i] = min(dp[i], dp[i-j] + card[j-1])
print(dp[N])


