N = int(input())
# 1개 또는 3개. 마지막 가져가면 게임 짐
# 상근이 먼저 시작

dp = [0] * (1001) # dp[i] : i번째 돌을 가져간 사람

dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'

for i in range(4, N+1):
    if dp[i-1] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

    if dp[i-3] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

if dp[N] == 'SK':
    print('CY')
else:
    print('SK')