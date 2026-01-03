N = int(input())
flowers = list(map(int, input().split()))

dp = [-1e10] * 101
# dp[i] : 1부터 100까지의 각 꽃의 아름다움 값 k에 대해서 i번째 꽃까지 둘러봤을 때 아름다움이 k로 끝나는 꽃다발의 가장 큰 아룸다움 값

dp[flowers[0]] = 0

for i in range(1, N):
    for j in range(1, 101):
        if dp[j] != -1e10:
            dp[flowers[i]] = max(dp[flowers[i]], dp[j] + (flowers[i] - j) ** 2)
print(max(dp))