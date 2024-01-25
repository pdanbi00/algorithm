A = int(input())
A_list = [0] + list(map(int, input().split()))
dp = [1] * (A+1)
for i in range(2, A+1):
    for j in range(1, i):
        if A_list[j] < A_list[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))