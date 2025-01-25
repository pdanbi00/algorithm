N = int(input())
dp = [i for i in range(N+1)]

# 6번째까지는 그 개수만큼이 최대
# 붙여넣기는 항상 3번 이하로 발생
# 참고 : https://hi-guten-tag.tistory.com/322
for i in range(6, N+1):
    dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4)

print(dp[N])