# 그래프에서 최단 경로를 구한느 플로이드 와샬 알고리즘으로 간으
# 시작점을 K로 해서 백트래킹.
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
visited[K] = 1
ans = 1e9
for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

def find_min(curr, cost, cnt):
    global ans
    if N == cnt:
        ans = min(ans, cost)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find_min(i, cost + board[curr][i], cnt + 1)
            visited[i] = 0

find_min(K, 0, 1)
print(ans)