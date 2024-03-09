# dp[i] : 수열의 i번째 수를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
N = int(input())
num_list = [0] + list(map(int, input().split()))
dp = [1] * (N+1)
for i in range(2, N+1):
    for j in range(1, i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))