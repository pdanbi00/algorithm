N = int(input())
boxes = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열 문제랑 같음
dp = [1] * N
# dp[i] : i를 마지막으로 갖는 부분 수열 중 길이의 최대값

for i in range(N):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))