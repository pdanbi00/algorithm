import sys
input = sys.stdin.readline

# dp[i]는 i일까지 상담을 하는 경우 최대 이익
N = int(input())
dp = [0] * (N+1)
data = [[0] * 2 for _ in range(N+1)]
for i in range(1, N+1):
    day, price = map(int, input().split())
    data[i][0] = day
    data[i][1] = price
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + data[i][0] - 1
    if fin_date <= N: # 최종일 전에 끝나는 경우
        dp[fin_date] = max(dp[fin_date], dp[i-1]+data[i][1])
print(max(dp))