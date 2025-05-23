max_len = len(bin(10**16)[2:])

dp = [0 for _ in range(max_len)]
dp[0] = 1
for i in range(1, max_len):
    dp[i] = 2 * dp[i-1] + (1<<i)

def suffix_sum(x):
    ans = x & 1 # 0번째 자리 수
    for i in range(max_len, 0, -1): # 가장 높은 자리수부터
        if x & 1 << i: # x가 i번째 자리에 값을 갖고 있다면
            ans += dp[i-1] + x - (1 << i) + 1
            x -= 1 << i
    return ans

A, B = map(int, input().split())
print(suffix_sum(B) - suffix_sum(A-1))