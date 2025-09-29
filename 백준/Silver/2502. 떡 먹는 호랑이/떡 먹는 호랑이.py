D, K = map(int, input().split())

dp = [''] * 31
dp[1] = 'A'
dp[2] = 'B'

for i in range(3, D+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] = "".join(dp[i])

a_cnt = dp[D].count('A')
b_cnt = dp[D].count('B')

for i in range(1, 100001):
    tmp = K - (i * a_cnt)
    if tmp % b_cnt == 0:
        print(i)
        print(tmp // b_cnt)
        break