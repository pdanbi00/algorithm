# N, M이 최대 8
# 고로 브루트포스로 3개씩 고르는 모든 경우를 확인
# 조합으로 3개 뽑아서 그 위치에 벽 세우고 bfs 각각 진행

# 바이러슥가 퍼지는 bfs 다 돌리고
# for 문 돌면서 0 개수 세서 안전영역 크게 구하기

from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0

def bfs(q):
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if newBoard[nr][nc] == 0:
                    newBoard[nr][nc] = 2
                    q.append((nr, nc))

arr = []

for i in range(N):
    for j in range(M):
        arr.append((i, j))

for n1, n2, n3 in combinations(arr, 3):
    if board[n1[0]][n1[1]] != 0 or board[n2[0]][n2[1]] != 0 or board[n3[0]][n3[1]] != 0:
        continue
    
    # 벽 새로 3개 세울 새로운 board 생성
    newBoard = [[0] * M for _ in range(N)]

    # 바이러스 담을 큐 생성
    q = deque()

    # 새로운 board 채우기
    for i in range(N):
        for j in range(M):
            newBoard[i][j] = board[i][j]
            #큐에 바이러스 시작 위치 입력해서 bfs 준비
            if board[i][j] == 2:
                q.append((i, j))
    
    # 새로운 벽 세우기
    newBoard[n1[0]][n1[1]] = 1
    newBoard[n2[0]][n2[1]] = 1
    newBoard[n3[0]][n3[1]] = 1

    # 바이러스 퍼트리기
    bfs(q)

    # 안전영역 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if newBoard[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
print(ans)
