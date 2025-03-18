N = int(input())
# dp[i] : i번째 작업이 끝나는 시간.
# 선행 작업이 없다면 0시간부터 시작하기 때문에 작업시간 그대로 저장
# 선행 작업 있다면 가장 늦게 끝나는 선행작업 시간을 더하기
dp = [0] * (N+1)
for i in range(1, N+1):
    time, cnt, *pre = map(int, input().split())
    dp[i] = time
    for j in pre:
        dp[i] = max(dp[i], dp[j] + time)

print(max(dp))