from collections import deque
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]] # 가장 마지막 요소가 바닥에 닿는 면
ans = 0

d = 0
r, c = 0, 0

dr = [0, 1, 0, -1] # 동, 남, 서, 북
dc = [1, 0, -1, 0] # 동, 남, 서, 북

# 칸에 대한 점수를 구하기 위한 C 구하기
def bfs(i, j, num):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == num and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    return cnt

while K > 0:
    # 1. 이동방향으로 굴러가기. 만약에 마지막 칸일 경우 방향 = (방향 + 2) % 2 해서 그 방향으로 굴리기
    n_r, n_c = r + dr[d], c + dc[d]
    if not (0 <= n_r < N) or not (0 <= n_c < M):
        d = (d+2) % 4
    #   1 - 1. 굴러가서 도착하는 위치 r, c 구하기
    r = r + dr[d]
    c = c + dc[d]

    #   1 - 2 구른 이후 주사위 전개도 변형
    # 동쪽일 경우
    if d == 0:
        new_dice = [dice[0], [dice[3][1], dice[1][0], dice[1][1]], dice[2], [0, dice[1][2], 0]]
    # 남쪽일 경우
    elif d == 1:
        new_dice = [dice[3], [dice[1][0], dice[0][1], dice[1][2]], [0, dice[1][1], 0], dice[2]]
    # 서쪽일 경우
    elif d == 2:
        new_dice = [dice[0], [dice[1][1], dice[1][2], dice[3][1]], dice[2], [0, dice[1][0], 0]]
    # 북쪽일 경우
    elif d == 3:
        new_dice = [[0, dice[1][1], 0], [dice[1][0], dice[2][1], dice[1][2]], dice[3], dice[0]]

    dice = new_dice
    
    # 2. bfs해서 점수(board[r][c] * cnt) 구하기. 그리고 ans에 추가
    tmp = bfs(r, c, board[r][c])
    ans += tmp * board[r][c]

    # 3. 이동방향 결정하기 board[r][c]와 주사위 아랫면 크기 비교
    if dice[-1][1] > board[r][c]:
        d = (d + 1) % 4
    elif dice[-1][1] < board[r][c]:
        d = (d + 3) % 4

    K -= 1

print(ans)