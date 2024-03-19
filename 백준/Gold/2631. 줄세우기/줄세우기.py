N = int(input())
order = []
for i in range(N):
    n = int(input())
    order.append(n)
# dp[i] : order의 i번째수를 마지막으로 가장 긴 증가하는 수열의 길이
dp = [1] * (N)
for i in range(1, N):
    for j in range(i):
        if order[i] > order[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N-max(dp))
