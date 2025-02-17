import sys
input = sys.stdin.readline

D, P = map(int, input().split())
dp = [1e9] + [0] * D # dp[i] : 파이프 길이가 i일 때 파이프 최대 용량

for _ in range(P):
    length, cost = map(int, input().split())
    dp_max = dp[:]
    for i in range(length, D+1):
        if dp_max[i-length]:
            dp[i] = max(dp[i], min(dp_max[i-length], cost))
print(dp[D])