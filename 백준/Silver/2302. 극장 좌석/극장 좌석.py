import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
vip = [int(input().rstrip()) for _ in range(M)]

dp = [0] * 41
dp[0] = 1 # vip가 연속으로 있으면 dp[0]을 사용할 텐데 한가지 경우니깐 1임.
dp[1] = 1 # 1
dp[2] = 2 # 1 2, 2 1
# dp[3] = 3  # 1 2 3, 2 1 3, 1 3 2

# 점화식 : dp[n] = dp[n-1] + dp[n-2]
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1

# vip 유무에 따라서 경우의 수 도출
if M > 0:
    tmp = 0
    for j in range(M):
        # vip들 사이에 몇개 있는지 계산해서 그 수 만큼의 자리가 있을 때 경우를 각각 곱해줌
        answer *= dp[vip[j] - 1 - tmp]
        tmp = vip[j]
    answer *= dp[N - tmp]
else:
    answer = dp[N]
print(answer)