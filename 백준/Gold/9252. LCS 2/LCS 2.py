# DP
word1 = [0] + list(input())
word2 = [0] + list(input())

# dp[i][j] : word1의 i번째 글자와 word2의 j번째 글자까지의 최장 공통 부분 수열

dp = [[''] * len(word2) for _ in range(len(word1))]

for i in range(1, len(word1)):
    for j in range(1, len(word2)):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i-1][j-1] + word2[j]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

ans = len(dp[len(word1)-1][len(word2)-1])
print(ans)
if ans != 0:
    print(dp[len(word1)-1][len(word2)-1])