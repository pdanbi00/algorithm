N = int(input())
T = [0] * (N)
P = [0] * (N)
dp = [0] * (N+1)
for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N-1, -1, -1):
    # i일에 상담을 하는게 퇴사일을 넘기면 상담 안한다.
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는거랑 상담 안하는거 중에 큰거 선택
        dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])
print(dp[0])