from collections import deque

N, M, P = map(int, input().split())
move = list(map(int, input().split()))
board = [[] for _ in range(N)]

for i in range(N):
    arr = list(input())
    for a in arr:
        if a == '.' or a == '#':
            board[i].append(a)
        else:
            board[i].append(int(a))

p_castle = [[] for _ in range(P)] # 각 플레이어가 갖고 있는 성 위치

visited = [[-1] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def sol(board, p_castle, distance, idx):
    q = deque()
    stack = []
    cnt = 0

    while p_castle[idx]:
        pr, pc = p_castle[idx].pop()
        q.append((pr, pc, 0))
        visited[pr][pc] = 0

    while q:
        r, c, dis = q.popleft()
        next_dis = dis + 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if next_dis > distance:
                break

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == '.' and visited[nr][nc] == -1:
                    if board[nr][nc] != idx:
                        cnt += 1
                        stack.append((nr, nc))
                        q.append((nr, nc, next_dis))
                        visited[nr][nc] = 0

    # 값 업데이트
    if cnt != 0:
        answer[idx] += cnt
        while stack:
            r, c = stack.pop()
            board[r][c] = idx
            p_castle[idx].append((r, c))
        return True
    return False

for i in range(N):
    for j in range(M):
        if board[i][j] != '.' and board[i][j] != '#':
            now_castle = board[i][j] - 1
            p_castle[now_castle].append((i, j))

# 정답값 기초로 만들어 놓기
answer = [0] * P
for idx in range(P):
    answer[idx] = len(p_castle[idx])

while 1:
    impossible = True
    for ppp in range(P):
        check = sol(board, p_castle, move[ppp], ppp)
        if check:
            impossible = False
    if impossible:
        break
print(*answer)