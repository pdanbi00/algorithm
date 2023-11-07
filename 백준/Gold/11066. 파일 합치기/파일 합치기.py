def solve():
    k = int(input())
    file = [0] + list(map(int, input().split()))
    tmp = [0 for _ in range(k + 1)]

    for i in range(1, k + 1):
        tmp[i] = tmp[i - 1] + file[i]

    # dp[i][j]는 i번째 파일부터 j번째 파일을 합치는 최소값
    dp = [[0] * (k + 1) for _ in range(k + 1)]

    for x in range(2, k + 1):
        for y in range(1, k + 2 - x):
            dp[y][y + x - 1] = min([dp[y][y + z] + dp[y + z + 1][y + x - 1] for z in range(x - 1)]) + (
                    tmp[y + x - 1] - tmp[y - 1])

    print(dp[1][k])


t = int(input())
for _ in range(t):
    solve()