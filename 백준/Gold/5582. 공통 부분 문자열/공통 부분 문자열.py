import sys
input = sys.stdin.readline
answer = 0
line1 = input().rstrip()
line2 = input().rstrip()

dp = [[0] * (len(line2) + 1) for _ in range(len(line1) + 1)]

for i in range(1, len(line1) + 1):
    for j in range(1, len(line2) + 1):
        if line1[i-1] == line2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)
print(answer)
