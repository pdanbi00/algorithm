A = int(input())
A_list = list(map(int, input().split()))
dp = [1] * A # dp[i]는 A_list의 i번째 수로 끝나는 최장수열의 길이
for i in range(1, A):
    for j in range(i):
        if A_list[j] < A_list[i] and dp[i] < (dp[j] + 1):
            dp[i] = dp[j] + 1
ans = max(dp)
print(ans)

ans_list = []
order = ans
for i in range(A-1, -1, -1):
    if dp[i] == order:
        ans_list.append(A_list[i])
        order -= 1
ans_list.reverse()
print(*ans_list)