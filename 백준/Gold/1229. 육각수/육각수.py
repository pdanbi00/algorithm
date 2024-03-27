N = int(input())
six = [1]
n = 2
num = 1
while num < N: # N보다 작은 육각수 구하기
    num = num + (4 * n) - 3
    six.append(num)
    n += 1

dp = [6] * (N+1) # dp[i] : i를 만들 수 있는 육각수의 최소
for s in six:
    if s <= N:
        dp[s] = 1
for i in range(N+1):
    for s in six:
        if i >= s:
            dp[i] = min(dp[i], dp[i-s]+1)
        else:
            break
print(dp[N])
