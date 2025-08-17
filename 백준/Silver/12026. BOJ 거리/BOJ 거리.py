N = int(input())
blocks = list(input())

dp = [1e9] * N
dp[0] = 0

for i in range(N):
    if dp[i] == 1e9:
        continue

    if blocks[i] == 'B':
        for j in range(i, N):
            if blocks[j] == 'O':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
    elif blocks[i] == 'O':
        for j in range(i, N):
            if blocks[j] == 'J':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
    elif blocks[i] == 'J':
        for j in range(i, N):
            if blocks[j] == 'B':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)

if dp[N-1] == 1e9:
    print(-1)
else:
    print(dp[N-1])