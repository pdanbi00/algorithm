# DP
# dp[i][j] : 백선수를 i명, 흑선수를 j명 영입했을 때 능력치의 최댓값

dp = [[0] * 16 for _ in range(16)]
while True:
    try:
        white, black = map(int, input().split())
        for w in range(15, -1, -1):
            for b in range(15, -1, -1):
                if w != 0:
                    dp[w][b] = max(dp[w-1][b]+white, dp[w][b])
                if b != 0:
                    dp[w][b] = max(dp[w][b-1] + black, dp[w][b])
    except:
        print(dp[15][15])
        break