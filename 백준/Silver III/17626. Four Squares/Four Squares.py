# dp로 풀기
# dp[i] : i를 만들때 필요로 하는 제곱 수들의 개수
# dp[N]을 구하면 됨
# 예를 들어서 dp[8]의 경우 8 이전에 존재하는 제곱수는 1, 4가 있다.
# 그러므로 dp[8]의 개수를 셀 수 있는 경우는 dp[1] + dp[7], dp[4] + dp[4]가 존재하는데
# 이를 구하기 위해선 n에서 각 제곱수들을 빼준 수의 dp값(여기서는 dp[7], dp[4]) 에다가 제곱수의 dp 값인 1을 더해주면 된다. (dp[1] = 1, dp[4] = 1)
# 즉, i에서 빼주기 위한 j의 범위는 1부터 int(i ** 0.5)까지의 수이고, i에서 제곱수들을 빼주는 식은 dp[i-(j ** 2)]이다.  (여기서 i가 8이므로 int(i ** 0.5)는 2가 되니까 j의 범위는 1부터 2)

from math import sqrt
n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    min_value = 4
    for j in range(1, int(sqrt(i))+1):
        min_value = min(min_value, dp[i-(j**2)] + 1)
    dp.append(min_value)
print(dp[n])