from collections import deque
def bfs(si, sj, h):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and board[ni][nj] > h:
                q.append((ni,nj))
                v[ni][nj] = 1

def solve(height):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > height and v[i][j] == 0:
                bfs(i, j, height)
                cnt += 1
    return cnt

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(100): # 비가 0부터 가장 높은 위치까지 잠기는 경우 보려고
    v = [[0]*N for _ in range(N)]
    result = max(result, solve(i))

print(result)
