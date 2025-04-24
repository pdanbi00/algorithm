dp = [float('inf')] * 101
# dp[i] : i개의 성냥개비로 만들 수 있는 가장 작은 수
# dp[i] : min(dp[i], dp[i-j] 연결 dp[j])
num_list = ['', '', 1, 7, 4, 2, 6, 8]
for i in range(2, 8):
    dp[i] = num_list[i]

for i in range(8, 101):
    for j in range(2, i-1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))


def find_big(num):
    result = '1' * (num // 2)
    if num % 2 == 1:
        result = '7' + result[1:]
    return int(result)

def find_small(num):
    return dp[num]

T = int(input())
for _ in range(T):
    N = int(input())
    print(find_small(N), find_big(N))

