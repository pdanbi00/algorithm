import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total = [[0] * N for _ in range(N)]

for i in range(N):
    t = 0
    for j in range(N):
        t += board[i][j]
        total[i][j] = t

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for j in range(x1-1, x2):
        ans += total[j][y2-1]
        if y1 - 2 >= 0:
            ans -= total[j][y1-2]
    print(ans)