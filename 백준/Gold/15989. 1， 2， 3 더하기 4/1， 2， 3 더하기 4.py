# DP
# 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 취급!!

dp = [1] * (10001) # 수를 1로만 표현하는 경우는 모든 수가 한 가지

# 숫자 2를 추가하는 경우
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 숫자 3을 추가하는 경우
for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])