# 처음에 board 다 돌면서 4개 이상 이어진 부분들 큐에 담기
# 연쇄 횟수는 큐에 같이 담아서 돌릴거임
# 한번 큐 돌리고 나서 한줄씩 내리기
from collections import deque
board = [list(input()) for _ in range(12)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0 # 연쇄 횟수

def bfs(r, c):
    q = deque()
    q.append((r, c))
    now = board[r][c] # 같은 색 4개 이상인지 확인해야하니깐 기준 색 지정
    arr = [] # 같은 색인 위치들 담기. 나중에 여기 터트리고 값들 내려줘야하니깐

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr  = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 12 and 0 <= nc < 6:
                if board[nr][nc] == now and visited[nr][nc] == False:
                    arr.append((nr, nc))
                    q.append((nr, nc))
                    visited[nr][nc] = True

    # 같은 색이 4개 이상 연결되어 있으면 터트리기
    if len(arr) >= 4:
        # 같은 열끼리 모으고, 행이 빠른 것부터 해줘야 됨.
        arr.sort(key=lambda x : (x[1], x[0]))
        for r, c in arr:
            board[r][c] = '_' # 빈자리랑 구분해서 방금 터진 곳이란 걸 표시
            boom.append((r, c))

while True:
    visited = [[False] * 6 for _ in range(12)]
    boom = [] # 터트린 곳들

    # 색이 같은 뿌요 4개 이상인 곳들 찾아서 터트리기
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and board[i][j] != '_' and not visited[i][j]:
                bfs(i, j)
    # 뿌요 터트린거 없으면 중단
    if len(boom) == 0:
        break
    # 나머지 뿌요들 아래로 떨어트리기
    for b in boom:
        r, c = b[0], b[1]
        for i in range(r, 0, -1):
            board[i][c] = board[i-1][c]
        board[0][c] = '.' # 맨 위에는 새로운 빈공간이 추가 됨
    ans += 1

print(ans)

'''
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
'''