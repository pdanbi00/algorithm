from collections import deque
from copy import deepcopy

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 우선순위를 위해서 왼쪽, 위쪽, 오른쪽
dr = [0, -1, 0]
dc = [-1, 0, 1]

def kill(gungs):
    new_board = deepcopy(board)
    visited = [[0] * M for _ in range(N)]

    cnt = 0
    for i in range(N-1, -1, -1):
        this_turn = [] # 이번 턴에 죽는 애들
        # 궁수별로 bfs 돌리면서 사정거리 안에서 가장 가까운 적군 찾기
        for gung in gungs:
            # 첫번째 값은 궁수 바로 위
            q = deque()
            q.append((1, i, gung))
            while q:
                distance, r, c = q.popleft()
                # 그 칸에 적군이 있으면
                if new_board[r][c] == 1:
                    this_turn.append((r, c))
                    if visited[r][c] == 0:
                        visited[r][c] = 1
                        cnt += 1
                    break

                if distance < D:
                    for p in range(3):
                        nr = r + dr[p]
                        nc = c + dc[p]
                        if 0 <= nr < N and 0 <= nc < M:
                            q.append((distance+1, nr, nc))
        # 공격할 애들 동시에 죽이기
        for r, c in this_turn:
            new_board[r][c] = 0
    return cnt

ans = -1
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            gungs = [i, j, k]
            tmp = kill(gungs)
            ans = max(ans, tmp)
print(ans)