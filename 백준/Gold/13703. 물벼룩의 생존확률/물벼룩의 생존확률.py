k, n = map(int, input().split())
# dp[i][j] : i초 j센치미터에서 수면에 닿아서 없어질 확율
dp = [[-1] * 130 for _ in range(64)]

def swim(sec, loc):
    if dp[sec][loc] != -1:
        return dp[sec][loc]

    if loc == 0:
        dp[sec][loc] = 2 ** sec # 위치가 0이 되면 나머지 시간은 어느 방향으로 가든 상관 없어서 남은 모든 경우의 수
        return dp[sec][loc]

    if sec == 0:
        return 0

    dp[sec][loc] = swim(sec-1, loc-1) + swim(sec-1, loc+1)
    return dp[sec][loc]

swim(n, k)

print(2 ** n - dp[n][k])