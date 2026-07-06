def solution(sticker):
    answer = 0
    N = len(sticker)
    if N == 1:
        return sticker[0]
    
    dp = [0] * 100001
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])
    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
    answer = max(answer, dp[N-2])
    
    dp = [0] * 100001
    if N == 2:
        return max(sticker)
    
    dp[1] =sticker[1]
    dp[2] = max(dp[1], sticker[2])
    for i in range(3, N):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    answer = max(answer, dp[N-1])

    return answer