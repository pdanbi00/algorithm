import sys
input = sys.stdin.readline

# 문제 조건에 제곱이 1000000보다 작다 했기 때문에 음수도 나올 수 있음!!
i = 0
while True:
    i += 1
    N = int(input())
    if N == 0:
        break
    dp = [list(map(int, input().split())) for _ in range(N)]

    # 두번째줄부터 계산
    dp[1][0] += dp[0][1] # 제일 위 가운데에서부터 시작하니깐
    dp[1][1] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][0])
    dp[1][2] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][1])

    for j in range(2, N):
        dp[j][0] += min(dp[j-1][0], dp[j-1][1])
        dp[j][1] += min(dp[j-1][0], dp[j-1][1], dp[j-1][2], dp[j][0])
        dp[j][2] += min(dp[j-1][1], dp[j-1][2], dp[j][1])
    print("%d. %d" %(i, dp[N-1][1]))