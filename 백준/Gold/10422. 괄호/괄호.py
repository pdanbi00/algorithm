# 괄호를 닫으려면 무조건 짝수
# 괄호 전체 개수를 n개라고 했을 때 첫번째 여는 괄호를 닫는 괄호가 i번째라고 해보자
# 첫번째 연 괄호랑 그걸 닫는 괄호 사이의 공간의 괄호 개수는 i-2개임
# i번째 이후의 공간 이후 괄호 개수는 n - (i-2 + 2) -> (n - i)개
# 결과적으로 dp[n] = dp[i-2] * dp[n-i]
import sys
input = sys.stdin.readline

dp = [0] * 5001
dp[0] = 1
for n in range(2, 5001, 2):
    for i in range(2, n+1, 2):
        dp[n] += dp[i-2] * dp[n-i]
    dp[n] %= 1000000007

T = int(input())
for _ in range(T):
    L = int(input())
    print(dp[L])